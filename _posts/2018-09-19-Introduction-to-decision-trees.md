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

{% include image.html url="/images/Example_decision_tree.png" caption="" max_width="100px" align="right" %}

This is an example of a decision tree, here Age, Student and Credit Rating Nodes are Decision nodes because they tell you which direction to go in a tree. And all the yes/no nodes are leaf nodes as they tell you the decision.

Now the problem remains is given a training data we have to generate decision tree. It is always possible that for a given training data we can generate many decision trees. So other question which arises is what should be the metric on which we decide to chose a particular decision tree. Like in linear regression we chose equation whose sum of squared error is minimum over the training data, similarly we will find a metric to chose a decision tree.
By choosing a bias we generally restrict the hypothesis space or we put preference on hypothesis space. Once we have chosen decision tree as hypothesis space we can put preference on it. In general the preference we use are smaller trees. By smaller trees we mean trees with low depth or/and trees with small number of nodes.
<hr>

## How to recursively build a tree (An example)
{% include image.html url="/images/Other_example_decision_tree.png" caption="" max_width="256px" align="right" %}
Lets say we have training data D and we want to build a tree with it. In the image we can see that we split the training data D at root using attribute A5 and by doing that we get 2 nodes. D1 is the training data with attribute A5 as ‘Y’ and D2 be training data with attribute A5 as ’N’. If we have a node with all training data have same label we stop the tree there or else at each node we have option to either grow the tree or to stop the tree, if we decide to grow the tree we have to further decide which attribute to split the data on. In the image let’s say that D2 have training data will same label so we stop the tree there but at D1 we can grow the tree because it contains the mixture of both the labels (considering training data have 2 labels). Now we have to use another attribute to split the data D1 using attribute A2 (here we are choosing attribute randomly and we will discuss later how to pick a attribute to make tree smaller). In the image D11 is the subset of data D1 which have attribute A2 as ‘Y’ and D12 have attribute A2 as ’N’. Like this we can recursively grow tree.

## Top-Down Induction of Decision Trees ID3

This is a basic framework of decision tree algorithm. At each node we do the following:-
<ol>
  <li>A is the best decision attribute for next node.</li>
  <li>Assign A as decision attribute for node.</li>
  <li>For each value of A create new descendant</li>
  <li>Sort training examples to leaf node according to the Lattribute value of the branch (This means split the training examples according to the attribute A chosen above).</li>
  <li>If all training examples are perfectly classified (same value of target attribute) stop, else iterate over new leaf nodes.</li>
</ol>

Here we have 3 questions,
<ol>
  <li>Given a partial decision tree which node to choose for the above algorithm</li>
  <li>For a particular node which is the best attribute to choose.</li>
  <li>When to stop splitting the tree.</li>
</ol>

## Learning Decision Tree

First we will look at criteria when to stop splitting decision tree, then we will move on to learn which attribute to split on.

<b>When to stop </b>
<ol>
  <li>When we have exhausted all the attributes and we don’t have any attributes to split on then we stop the splitting because we have no opther option.</li>
  <li>When all the examples of the node have same target value then we can stop the splitting.</li>
  <li>We should also stop splitting if we have too few examples to split on. Here few is a subjective term and its up-to user to decide how many examples are too few for them.</li>
</ol>

<b> Which attribute to split on </b>
<br>
Earlier we have discussed about bias criteria which says that we prefer smaller decision trees, so we can think of a heuristic method of choosing an attribute so that based on that attribute the decision tree is expected to be smaller.
One way to choose the attribute is to choose an attribute splitting among which gives smallest error. For example if we choose an attribute and split the training data, we will have new nodes with subset of training data and if that subset of training data have mixture of target value then we would prefer to split on attribute such the the new nodes have few mixtures of target value i.e. one type of target value should be more dominating than other.
We have few mathematical measures based on which we decide which attribute to choose at a particular node, and out of that few we will discuss about <b>Entropy</b> and <b>Information Gain</b>.

