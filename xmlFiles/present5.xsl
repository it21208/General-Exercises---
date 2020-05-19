<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
		<head>
			<title>QUERY_3</title>
		</head>
		<body bgcolor="#ffff99">
			<center>
				<h1><u>five query</u></h1>
			</center>
			<ul>
				<xsl:for-each select="cars_to_rent/car/main_characteristics">
					<xsl:if test="CO2_emissions &gt; 110">
						<li>
							<xsl:value-of select="/cars_to_rent/car/manufacturer_brand"/>
						</li>
					</xsl:if>
				</xsl:for-each>
			</ul>
		</body>
	</html>
</xsl:template>

</xsl:stylesheet>