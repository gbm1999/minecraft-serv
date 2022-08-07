import os, time, subprocess, signal

os.system('heroku-php-apache2 &')
print("**script**: starting web")
time.sleep(10)
os.system('nohup node --max-old-space-size=460 fetchworld.js > js.out & ')
print("**script**: fetching world...")
time.sleep(2)

while open('js.out', 'r').read().find('fetched world folder') <= -1:
    time.sleep(10)


print("**script**: world fetched!")
time.sleep(1)
os.system('unzip -o world.zip')
time.sleep(5)
print("**script**: starting server")
os.system('nohup java -Xmx500m -jar server.jar > nohup.out &')

while open('nohup.out', 'r').read().find('Done') <= -1:
    time.sleep(10)
        
print("**script**: server has started!")
time.sleep(10)
print("**script**: starting ngrok tcp")
os.system('ngrok tcp -region eu 25565 &')
time.sleep(10)

while True:
    print("**script**: saving world...")
    os.system('zip -FSr world.zip world')
    time.sleep(10)
    os.system('node --max-old-space-size=260 savetodb.js')
    print("**script**: world saved!")
    time.sleep(10)


