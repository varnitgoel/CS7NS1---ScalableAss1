echo Provide your port no :
read var
echo The server is on port no : $var

python server.py "$var"
