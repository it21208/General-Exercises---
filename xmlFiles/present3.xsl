<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="2.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<!-- <xsl:param name="pSortField" select="'monthly_leasing[@without_tax='false']'"/>
	<xsl:param name="pSortOrder" select="'descending'"/>
	<xsl:param name="pSortDataType" select="'number'"/> -->

	<xsl:template match="cars_to_rent">
		<html>
			<head>
				<title>QUERY_3</title>
			</head>
			<body bgcolor="#ffff99">
				<center>
					<h1>
						<u>third query</u>
					</h1>
				</center>
				<table border="1" align="center">
					<tr bgcolor="yellow">
						<th>etaireia kataskevis</th>
						<th>model</th>
						<th>monthly_leasing</th>
					</tr>
					<xsl:for-each select="//monthly_leasing[@without_tax='false']">
						<!-- <xsl:sort select="monthly_leasing" order="descending"/> -->
						<xsl:sort select="@without_tax='false'" order="descending"/>
						<tr>
							<!-- <td> <xsl:value-of select="/cars_to_rent/car/manufacturer_brand"/> </td>
							<td> <xsl:value-of select="/cars_to_rent/car/manufacturer_brand/model"/> </td>
							<td> <xsl:value-of select="/cars_to_rent/car/economic_info_leasing/monthly_leasing"/> </td> -->
							<td> <xsl:value-of select="//manufacturer_brand"/> </td>
							<td> <xsl:value-of select="//model"/> </td>
							<td> <xsl:value-of select="//monthly_leasing"/> </td>
						</tr>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>