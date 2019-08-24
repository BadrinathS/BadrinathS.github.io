---
layout: post
title: "Introduction to Decision Trees"
description: "Basics of building a decision tree"
categories: ["Machine Learning", "Decision Tree", "Entropy"]
location: "Guwahati, India"
---
In this section we will discuss about what is a decision tree, how its build, Entropy, Information Gain and overfitting.
<h1> What is a decision tree </h1>

Decision tree is a classifier in the form of a tree (here by tree we mean<a href="https://en.wikipedia.org/wiki/Tree_(data_structure)"> computer science tree</a>). This tree generally have 2 types of nodes i.e. Decision Nodes and Leaf Nodes.

## Decision Nodes

Decision nodes specify a choice or a test based on which we can decide which direction we can go on a tree. The test is usually done on a feature or attribute of the data. Unlike tree decision tree can have more than 2 branches depending on situation.

## Leaf Nodes

It indicates classification of the example or the value of example. So in general, given a data we start with root node and based on the test (on decision node) we go to corresponding branch and continue doing that till we reach a leaf node which contains the value (it can be predicted value of example, classification, regression or probability).

## Example

{% include image.html url="images/Example_decision_tree.png" caption="" max_width="100px" align="right" %}

This is an example of a decision tree, here Age, Student and Credit Rating Nodes are Decision nodes because they tell you which direction to go in a tree. And all the yes/no nodes are leaf nodes as they tell you the decision.

Now the problem remains is given a training data we have to generate decision tree. It is always possible that for a given training data we can generate many decision trees. So other question which arises is what should be the metric on which we decide to chose a particular decision tree. Like in linear regression we chose equation whose sum of squared error is minimum over the training data, similarly we will find a metric to chose a decision tree.
By choosing a bias we generally restrict the hypothesis space or we put preference on hypothesis space. Once we have chosen decision tree as hypothesis space we can put preference on it. In general the preference we use are smaller trees. By smaller trees we mean trees with low depth or/and trees with small number of nodes.
<hr>

## How to recursively build a tree (An example)
