# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')

    #Fill in start -are you accepting connections?
    connectionSocket, addr = 
    #Fill in end
    
    try:
      #Fill in start
      message = connectionSocket.recv(1024).decode() #gets https request
      #Fill in end 
      
      #get filename from GET request
      filename = message.split()[1]
      
      #Fill in start
      f = open(filename[1:], "r")
      #fill in end
      

      #Fill in start
      #make response headers
      outputdata = "HTTP/1.1 200 OK\r\n"
      outputdata += "Content-Type: text/html; charset=UTF-8\r\n"  
      outputdata += "Server: MyServer\r\n"   #changed server name
      outputdata += "Connection: close\r\n\r\n"  #need empty line after headers
            
      #get file contents
      filedata = ""
      for line in f:  #read file line by line
        filedata += line
            
            #send everything at once
            connectionSocket.send(outputdata.encode() + filedata.encode())
            #Fill in end
            
            connectionSocket.close()
            
        except:  #file not found
            #Fill in start
            #send 404 error
            err = "HTTP/1.1 404 Not Found\r\n"
            err += "Content-Type: text/html; charset=UTF-8\r\n" 
            err += "Server: MyServer\r\n"
            err += "Connection: close\r\n\r\n"
            err += "<html><h1>404 Not Found</h1></html>"
            
            connectionSocket.send(err.encode())
            #Fill in end
            
            #Fill in start
            connectionSocket.close()  #close connection
            #Fill in end

if __name__ == "__main__":
    webServer(13331)