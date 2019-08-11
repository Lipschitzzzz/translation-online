import urllib.request
import urllib.parse
import json
import tkinter as tk
from tkinter.filedialog import askopenfilename
def translate(text):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data['i'] = text
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1528204978533'
    data['sign'] = '1114bcc7451adcd9d9647422d6d8fa3b'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode("utf-8")
    response = urllib.request.urlopen(url, data)
    html = response.read().decode("utf-8")
    result = json.loads(html)
    result = result['translateResult'][0][0]['tgt']
    return result
a = 'apple,pear,bear'
main = tk.Tk()
main.title = '有道翻译'
text1 = tk.Text(main)
text2 = tk.Text(main)
def Button1():
    result = 'error'
    result = translate(text1.get("0.0","end"))
    text2.delete("0.0","end")
    text2.insert("0.0",result)
def Button2():
    result = 'error'
    with open(askopenfilename()) as f:
        result = f.read()
    text1.insert("0.0", result)
button1 = tk.Button(main, text = '打开文件', command = Button2)
button2 = tk.Button(main, text = '翻译', command = Button1)
text1.pack()
text2.pack()
button1.pack()
button2.pack()
main.mainloop()