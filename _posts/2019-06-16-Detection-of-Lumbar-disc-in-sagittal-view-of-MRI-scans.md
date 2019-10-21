---
layout: post
title: "Detection of Lumbar disc in sagittal view of MRI scans"
description: "MRI scans, lumbar disc detection"
categories: ["Machine Learning", "Computer Vision", "Medical Imaging", "MRI Scans"]
location: "Bangalore, India"
---

In this post we will discuss about an unsupervised method which can be used to detect lumbar disc in sagittal view of MRI scans.
MRI machines take image of patient in 3 different planes, i.e. Sagittal, Coronal and Axial. To know more about working of MRI machines and different planes, refer here.
In sagittal view of MRI, we can clearly see vertebrae and lumbar disc running parallel to spine. Below image shows a sample sagittal view and one of the lumbar disc and vertebrae.



Detecting all the lumbar disc in a particular sagittal view of MRI through image processing method is not simple problem to solve because each sagittal view have variable number of lumbar disc, size, shape and orientation of each disc is different also each image have different pixel distributions.
When we get MRI scan of a patient, we get images from all 3 planes, so by using that we can figure out projection of other 2 plane in sagittal view. We get projection as a line is the corresponding plane is horizontal with coordinate axis, otherwise it will be a trapezium. When we project 2 opposite sides of axial plane to sagittal planes, we get line(or 2 line if axial plane is not horizontal), generally in case of MRI machines that line passes through lumbar disc or vertebrae.
