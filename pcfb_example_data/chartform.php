<html>
<body>
<code>
<strong>A plot of my data </strong><br>

<?php
	checkforinput(); // defined below
	$filename = "data.txt";
	$data = file($filename);
	
// $data are an array in the format 1,2,3,100 or on their own lines
// add new data with  echo "100" >> ~/Sites/data.txt

//http://chart.apis.google.com/chart?cht=lc&chs=200x125&chd=t:40,60,60,45,47,75,70,72&chm=s,0000FF,0,-1,5

	$usedata=$data[0];
	
	$alldata=trim(join(",", $data));
	$subsetdata=str_replace("\n",'',$alldata);
	$allvals = explode(',',$subsetdata);	
	$usewidth=count($allvals)*23; # the width of the bar chart.
	if ($usewidth>400) { $usewidth=400; }
	
//	print_r($allvals);
	echo "<br>";
 	echo "DATA:".$subsetdata."<br>";
	echo "<br>";
	echo "<img src=\"http://chart.apis.google.com/chart?cht=bvs&chco=4D89F9&chs=$usewidth"."x125&chbh=a&chd=t:$subsetdata\">";
	echo "<br>";
	echo "<br>";
	echo "<img src=\"http://chart.apis.google.com/chart?cht=lc&chs=200x125&chm=s,0000FF,0,-1,5&chd=t:$subsetdata\">";
	echo "<br>";

$seconds=time();
$timenow=substr(strval($seconds), -2);

?> 

<?php
function checkforinput(){
	$filename="data.txt";
	if (isset($_POST['newvalue'])){
		$holder=intval($_POST['newvalue']);
		$msg=strval($holder);
		echo "Added $msg to data ";
		$fp = fopen($filename, "a"); # w = write to the file only, create file if it does not exist, discard existing 
		fwrite ($fp, $msg."\n");
		fclose($fp);
	}
}
?>

<form action="chartform.php" method="post">
NewValue: <input type="text" name="newvalue" value="<?=$timenow?>"/>
<input type="submit" />
</form>

</code>
</body>

</html>
