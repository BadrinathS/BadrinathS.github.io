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


## Image of sagittal view with all the lines

So using that lines, we have information of orientation of all the lumbar disc and vertebrae. Below image (right)contains a yellow line, which is the projection of axial plane in sagittal view (In this case axial plane was perpendicular to sagittal plane so there was just one line instead of 2).

If we project all the axial planes present in a particular MRI case, we will get group of lines each will pass through either through lumbar disc or vertebrae.
We crop out few good images of lumbar disc from sagittal scans, and use that as our templates for template matching in sagittal image. Now if we do template matching we get lots of possible locations (some of which are repetitive and some are false positive). To remove repetitive detection we calculate the intersection between each detection, if they surpass some threshold then we assume those detection to be made on same object and remove one of them (Selecting which to remove is another challenge as we still don’t know which detection is more aligned with the object).
Removing false positives is also a challenging task, as we don’t know where the object (lumbar disc) is, but we can minimise it. We can take the help of lines which we get when we project axial scans to sagittal scans. We know that lumbar disc should lie somewhere in the line, so we put additional condition that if the detection doesn’t have intersection with the line then we reject that detection right away and keep all other detection under consideration for further filter.
Here, we have the detection after first stage of filtering through intersection of lines. Now we find the intersection of each detection with the lines, since it’s the intersection between line and a rectangle, so there can be 2 detection. We are taking the point which is leftmost compared to other point (You will see further it doesn’t matter which point we take, but we have to maintain order i.e. if we decide to take leftmost then we will choose leftmost for every detection, if there is one detection then we take that as it is).
Calculating all detection points, we now fit a polynomial through polynomial fitting. We now evaluate multiple polynomial by shifting the polynomial in x axis by constant (this can be done by scaling the x coordinates accordingly).
Here we have multiple polynomial which are parallel to each other (parallel is not a good term to describe it, but i guess you get the idea). Given a polynomial f(x), we calculate distance from the mid point of each detection (lets say (x1, y1)) to the polynomial i.e.|y-f(x)|. We sum the distance for each mid point of detection for a given polynomial and get total distance as D. After calculating D for each polynomial we choose the polynomial with lowest D.
Our final detection will be all the detection which intersect with the polynomial and reject other detections.
This method is completely unsupervised, this method is dependent on the quality of template, quality of MRI scans. And this is a huge parameter. As with not so good quality templates will lead to false detections. False detection will lead to weird final results.
With the variety of scan quality, detection of lumbar disc can be better handled through supervised method (like object detection, segmentation map etc).
In next post I will discuss about measurement of spinal canal diameter.
I hope you found this helpful. Please suggest improvements regarding the post and also any technical mistakes. I would really appreciate any suggestions and feedback.
