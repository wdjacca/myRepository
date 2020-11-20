<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns="http://www.w3.org/1999/xhtml"
    version="3.0">
    
    <xsl:output method="xhtml" encoding="utf-8" doctype-system="about:legacy-compat"
        omit-xml-declaration="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Montage of a Dream Deferred</title>
                <link rel="stylesheet" type="text/css" href="chanXSLTexercise3.css"/>
                <link rel="stylesheet" type="text/css" href="https://use.typekit.net/jkx1xou.css"/>
                <link rel="stylesheet" type="text/css" href="https://use.typekit.net/jkx1xou.css"/>
                <link rel="stylesheet" type="text/css" href="https://use.typekit.net/jkx1xou.css"/>
            </head>
            <body>
                <xsl:apply-templates select="descendant::poem[following-sibling::title]"/>
                
                <h1><xsl:apply-templates select="descendant::title"/></h1>
                <h2>by Langston Hughes</h2>
                
                <xsl:apply-templates select="descendant::poem[preceding-sibling::title]"/> 
                
            </body>
        </html>      
    </xsl:template>
    
    <xsl:template match="poem">
        <xsl:if test="poemTitle">
            <h3>
                <xsl:apply-templates select="poemTitle"/><!-- jkc: I don't know how to get the poemTitle to only print once, is there a if [detail1] and not [detail2] code I can use?-->
            </h3>
        </xsl:if>
        <xsl:if test="@cont">
            <h3 class="continued">
                <xsl:apply-templates select="poemTitle"/>
            </h3>
        </xsl:if>
        <xsl:if test="body">
            <section class="body">
                <xsl:apply-templates select="body"/>
            </section>
        </xsl:if>
    </xsl:template>
    <xsl:template match="body">
        <xsl:if test="stanza">
            <div class="stanza">
                <xsl:apply-templates select="stanza"/>
            </div>
        </xsl:if>
    </xsl:template>
    <xsl:template match="line">
            <p>
                <xsl:apply-templates/>
            </p>
    </xsl:template>
    <xsl:template match="format[@wordType='italics']">
        <em>
            <xsl:apply-templates/>
        </em>
    </xsl:template>
    <xsl:template match="format[@wordType='underline']">
        <em class="underline">
            <xsl:apply-templates/>
        </em>
    </xsl:template>
    <xsl:template match="format[@wordType='caps']">
        <em class="caps">
            <xsl:apply-templates/>
        </em>
    </xsl:template>
    <xsl:template match="format[@margin='ind1']">
        <em class="ind1">
            <xsl:apply-templates/>
        </em>
    </xsl:template>
    <xsl:template match="format[@margin='ind2']">
        <em class="ind2">
            <xsl:apply-templates/>
        </em>
    </xsl:template>
</xsl:stylesheet>
<!-- jkc: I did not manage to finish the line number part, but I think all the indent part worked -->
