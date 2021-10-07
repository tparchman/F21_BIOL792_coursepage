<html>
<body>
<code>
<strong>A plot of my data </strong><br>

<?php
	$filename = "data.txt";
	$data = file($filename);
	
// $data are an array in the format 1,2,3,100
// add new data with  echo ",100" >> ~/Sites/data.txt
//http://chart.apis.google.com/chart?cht=lc&chs=200x125&chd=t:40,60,60,45,47,75,70,72&chm=s,0000FF,0,-1,5

//$subsetdata=str_replace("\n",",",$data[1]);
	$usedata=$data[0];
	
//	$alldata=trim(join(",", $data));
//	$subsetdata=str_replace("\n","",$alldata);
	
	echo "<br>";
// 	echo "ARRAY1: XX$data[1]XX";
// 	echo "ALLDATA: $alldata<br>";
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