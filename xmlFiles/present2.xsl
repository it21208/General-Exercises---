<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="2.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<html>
			<head>
				<title>QUERY_2</title>
			</head>
			<body bgcolor="#ffff99">
				<center>
					<h1>
						<u>second query</u>
					</h1>
				</center>
				<table border="1" align="center">
					<tr bgcolor="yellow">
						<th>etaireia kataskevis</th>
						<th>model</th>
						<th>description of model</th>
						<th>color</th>
					</tr>
					<xsl:apply-templates select="cars_to_rent/car">
						<xsl:sort select="manufacturer_brand" order="ascending"/>
					</xsl:apply-templates>
				</table>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="car">
		<tr>
			<td>
				<xsl:value-of select="manufacturer_brand"/>
			</td>
			<td>
				<xsl:value-of select="manufacturer_brand/model"/>
			</td>
			<td>
				<xsl:value-of select="extra_car_info/@mini_model_description"/>
			</td>
			<td>
				<xsl:value-of select="extra_car_info/@color"/>
			</td>
		</tr>
	</xsl:template>

</xsl:stylesheet>