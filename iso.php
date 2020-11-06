<html>
	<head>
	<title>Can I haz ISO standardz?</title>
	<meta charset="UTF-8" />
	<script id="data" type="application/json"><?php include('iso_standards.json'); ?></script>
	<script>
		var jsonData = JSON.parse(document.getElementById('data').textContent);
		var codes = Object.keys(jsonData);
		var standards = Object.values(jsonData);
		var n_standards = codes.length;

		function getRandomStandard() {
			var idx = Math.floor(Math.random() * n_standards);
			title_field = document.getElementById("iso_title");
			title_field.textContent = standards[idx];
			
			code_field = document.getElementById("iso_code");
			code_field.textContent = codes[idx];
		}
	</script>
	<style>
		body {
			margin: 0px;
		}

		article {
			text-align: center;
			margin: 1em;
		}

		#iso_code {
			font-size: 3em;
			font-family: DejaVu Sans, Verdana, serif;
		}

		#iso_title {
			font-size: 2em;
			font-family: DejaVu Sans, Verdana, serif;
			width: 80%;
			margin: auto;
			text-align: justify;
		}
	</style>
	</head>

	<body>
		<article>
		<button onclick="getRandomStandard()">I ❤️  me some good standard, more!</button>
		<h1 id="iso_code"></h1>
		<h2 id="iso_title"></h2>
		</article>
	</body>
</html>
