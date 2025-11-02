
import ollama


MODEL='gemma3:1b'
def translate(text,toLang='中文'):
    X='你是一个翻译API，你需要把用户的输入翻译成'+toLang+'. 只需要回答翻译.'#
    stream = ollama.chat(
        model=MODEL,
        messages=[{'role':'system','content':X},{'role': 'user', 'content': text}],
        stream=True,
    )
    res=''
    for chunk in stream:
        i=chunk['message']['content']
        res+=i
    res=res.replace('\n','')
    return res

if __name__ == '__main__':
    text='hello world'
    print(translate(text,'中文'))