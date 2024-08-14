import openai as _openai

_client = _openai.OpenAI()
_gpt_generated_files = set()


def _get_chat_response(system, *prompts):
    response = _client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            *({"role": "user", "content": prompt} for prompt in prompts)
        ]
    )
    return response.choices[0].message.content


def _generate_name():
    import random
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_', k=20))


def auto(prompt: str, save_generated_code: bool = True):
    """
    Annotate a function that should be generated by GPT.
    :param prompt: The prompt string.
    :param save_generated_code: Whether to save the generated code to a new source file. If it is True, then a *.gpt-generated.py file containing the GPT-generated code will be generated.
    """
    def inject(func):
        code = func.__code__
        flags = code.co_flags
        varsnames = list(code.co_varnames)[:code.co_argcount + (flags & 8) + (flags & 4)]
        for k in func.__annotations__:
            if k != 'return':
                annotation = repr(func.__annotations__[k])
                if annotation.startswith("<class '") and annotation.endswith("'>"):
                    annotation = annotation[8:-2]
                varsnames[varsnames.index(k)] += ': ' + annotation
        if flags & 8:
            varsnames[-1] = '**' + varsnames[-1]
            if flags & 4:
                varsnames[-2] = '*' + varsnames[-2]
        elif flags & 4:
            varsnames[-1] = '*' + varsnames[-1]
        func_def = 'def %s(' + ', '.join(varsnames) + ')'
        if 'return' in func.__annotations__:
            annotation = repr(func.__annotations__['return'])
            if annotation.startswith("<class '") and annotation.endswith("'>"):
                annotation = annotation[8:-2]
            func_def += ' -> ' + annotation
        func_def += ':'
        
        new_name = _generate_name()
        func_def_new = func_def % new_name
        func_def = func_def % func.__name__
        
        while True:
            response = _get_chat_response(
                "You are a Python expert who can implement the given function.",
                f"Read this incomplete Python code:\n```python\n{func_def}\n```",
                f"Complete the Python code that follows this instruction: '''{prompt}'''. If you use import statements, they should be placed inside the function body. Your response must start with code block '```python\n{func_def}\n'."
            )
            if response.startswith('```python\n') and response.endswith('```'):
                response = response[10:-3].strip()
                try:
                    response1 = response.replace(func_def, func_def_new)
                    exec(response1)
                    new_func = eval(new_name)
                    if save_generated_code:
                        filename = code.co_filename + '.gpt-generated.py'
                        with open(filename, 'a' if filename in _gpt_generated_files else 'w', encoding='utf8') as f:
                            f.write('@gpt(')
                            f.write(repr(prompt))
                            f.write(')\n')
                            f.write(response)
                            f.write('\n\n\n')
                        _gpt_generated_files.add(filename)
                    return new_func
                except:
                    pass
    return inject
