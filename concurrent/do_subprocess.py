__author__ = 'shenyao'
import subprocess
# print("$ nslookup www.python.org")
# r=subprocess.call(['nslookup','www.python.org'])
# print("Exit code:",r)

#如果子进程还需要输入
print("$ nsloopup")
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode("utf-8"))
print(output.decode('latin-1'))
print('Exit code:',p.returncode)