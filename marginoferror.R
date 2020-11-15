#!/usr/bin/Rscript

#need standard error and critical z value

args <- commandArgs(trailingOnly = TRUE)

criticalz=as.numeric(args[1]) 
standarderror=as.numeric(args[2])

marginoferror=criticalz*standarderror
write(marginoferror, "")
