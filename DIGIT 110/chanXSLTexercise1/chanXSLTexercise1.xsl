<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs math xd"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    xmlns="http://www.tei-c.org/ns/1.0"
    version="3.0">
    <xd:doc scope="stylesheet">
        <xd:desc>
            <xd:p><xd:b>Created on:</xd:b> Nov 10, 2020</xd:p>
            <xd:p><xd:b>Author:</xd:b> jacca</xd:p>
            <xd:p></xd:p>
        </xd:desc>
    </xd:doc>
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="emph">
        <hi rend="italics">
            <xsl:apply-templates/>
        </hi>
    </xsl:template>
    <xsl:template match="head/l">
        <xsl:apply-templates/>
        <lb/>
    </xsl:template>
    <xsl:template match="div[@type ='book'][1]">
        <div type="book" n="1">
            <xsl:apply-templates/>
        </div>   
    </xsl:template>
    <xsl:template match="div[@type ='book'][position()!='1']">
        <div type="book" n= "{count(following-sibling::div[@type='book'])+1}">
            <xsl:apply-templates/>
        </div>   
    </xsl:template>
    <xsl:template match="div[@type ='chapter'][1]">
        <div type="chapter" n="1">
            <xsl:apply-templates/>
        </div>   
    </xsl:template>
    <xsl:template match="div[@type ='chapter'][position()!='1']">
        <div type="" n= "{count(following-sibling::div[@type='chapter'])+1}">
            <xsl:apply-templates/>
        </div>   
    </xsl:template>
    
</xsl:stylesheet>