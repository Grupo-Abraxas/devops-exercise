# -*- coding:utf-8 -*-
from flask import Flask, request
import os

app = Flask(__name__)

contador = 0

@app.route("/", methods=["GET", "POST"])
def hello():
	global contador
	if request.method == "POST":
		contador += 1

	server_addr = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]

	html = """
			 	<!doctype html>
				<html lang="es">
				<head>
    				<title>¡Hola Mundo!</title>
    				<meta charset="utf-8">
    				<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    				<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
  				</head>
  				<body>
				<div class="container">
					<div class="jumbotron mt-3">
    						<h1>¡Hola mundo!</h1>
					</div>

					<div class="alert alert-primary" role="primary">
						Peticiones POST: %s <br />
						Servidor: %s
					</div>
				</div>

				<footer class="footer">
      					<div class="container">
        					<span class="text-muted">Abraxas DevOps Test.</span>
      					</div>
    				</footer>
					
    				<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    				<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    				<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
  				</body>
				</html>
		""" % (contador, server_addr)
	return html


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)
