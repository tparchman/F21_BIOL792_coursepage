<html>
<body>
<code>
<strong>A plot of my data </strong><br>

<?php
	$filename = "data.txt";
	$data = file($filename);
	$subsetdata=$data[0];
	
	echo "<br>";
 	echo "DATA:".$subsetdata."<br>";
	echo "<br>";
	echo "<img src=\"http://chart.apis.google.com/chart?cht=bvs&chco=4D89F9&chs=200x125&chbh=a&chd=t:$subsetdata\">";
	echo "<br>";
	echo "<br>";
	echo "<img src=\"http://chart.apis.google.com/chart?cht=lc&chs=200x125&chm=s,0000FF,0,-1,5&chd=t:$subsetdata\">";
	echo "<br>";

?> 
</code>
</body>

</html>