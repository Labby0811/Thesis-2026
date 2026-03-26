#!/usr/bin/env perl

# Set the main file to compile
$main_name = 'tesi';

# Use PDF mode
$pdf_mode = 1;

# Enable synctex for better editor integration
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode';

# Only process the main file, ignore other tex files
@default_files = ('tesi.tex');

# Automatically remove generated files on clean
$cleanup_includes_generated = 1;
$cleanup_includes_curated = 1;
