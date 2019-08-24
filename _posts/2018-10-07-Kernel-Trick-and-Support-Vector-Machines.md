---
layout: post
title: "Kernel Trick and Support Vector Machines"
description: "What is kernel trick and its use in support vector machines"
categories: ["Machine Learning", "Kernel Trick", "Support Vector Machines"]
location: "Guwahati, India"
---

This page is about giving intuition of kernel trick and try to make it easy to adapt to support vector machines.
<br>
<br>
I first encountered kernel trick when I was learning about support vector machines in course “Pattern Recognition and Machine Learning” at IIT Guwahati. At first it didn’t make any sense to me as it was very absurd and opposite to how I use to think. But after going through various blogs and videos discussing with professor, I realized that it was quite simple and straight forward. Here I will try to put it in simple terms. Any feedback is highly appreciated.

## Kernel Trick

It is a technique which is used to save us from lots of computations in few algorithms. This method is so powerful that people start calling it as trick instead of a method or technique. Lets start by stating Cover’s Theorem

## <sub> Cover's Theorem </sub>
Cover’s Theorem state that, A complex pattern-classification problem, cast in a high-dimensional space nonlinearly, is more likely to be linearly separable than in a low-dimensional space, provided that the space is not densely populated.
<br>
<br>
Or in simple terms, given a set of training data that is not linearly separable, one can transform it into a training set that is linearly separable by mapping it into a possibly higher-dimensional space via some non-linear transformation.

{% include image.html url="/images/cover_theorem.png" caption="" max_width="100px" align="right" %}

Why do we choose non linear transformation? I will leave this to reader to ponder upon. (Little hint:- Does linearly transforming training set changes the nature of non linearity it already posses?). This theorem provides hope that every classification can be reduced to simple linearly separable problem. The only thing that we need to take care is to find the appropriate non linear transformation.

## <sub>How Kernel trick is applicable in Support Vector Machines</sub>

If you have read about <a href="https://en.wikipedia.org/wiki/Support-vector_machine" target="_blank">support vector machines</a> you would know that we are trying to minimize the objective function subject to various conditions. We apply <a href="https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions" target="_blank"> KKT conditions </a> to simplify the objective.

In the dual optimization problem we have below expression
<br>
{% include image.html url="/images/dual_optimization.png" caption="" max_width="100px" align="right" %}
<br>
Here w and b is the weight and bias vector. The zeta, lambda and mu is used in KKT conditions for constraints.
<br><br>
So now we change the SVM optimization problem to dual problem, which then looks like this.
<br>
{% include image.html url="/images/svm_optimization.png" caption="" max_width="100px" align="right" %}
<br>
In this expression we see the term x_i*x_j (its little tough to write mathematical expression in Medium), so that is the term where we use the trick. That term represents the dot product of the vector x_i and x_j.
<br>
<br>
If we want to use Cover’s theorem in this data set to change it to higher dimensional data, we need to find the correct dimension and correct transformation.
But if we look the expression closely, it deals with the dot product of the vectors. So even though we know the correct dimension and correct transformation to change our data to higher dimensional data, to apply SVM on the data we just need the dot product of the data so that we can put on the dual expression stated above. This is what kernel trick is. Kernel Trick saves us from all the hassle of knowing the correct dimension and correct transformation of changing the data and just leave us to know the dot product which we can use in the above expression.
<br>
<br>
By avoiding using the transformation we save ourselves from lots of unnecessary computation.
<br>
<br>
Please comment your suggestions to improve writing so I can write better post. Thanks

{% include test_disqus.html %}
