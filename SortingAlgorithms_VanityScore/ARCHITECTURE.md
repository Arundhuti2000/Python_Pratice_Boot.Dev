# 🏗️ Project Architectural Overview

## Project Composition

### File Type Distribution
- **documentation**: 1 files (25.0%)
- **python**: 2 files (50.0%)
- **web**: 1 files (25.0%)

### Source Path
`D:\Personal Projects\Python Practice\SortingAlgorithms_VanityScore`

## 📋 Project Overview
The project's primary purpose is to sort a list of influencers based on their vanity score. The main objectives are to provide an easy-to-use and efficient way to calculate and sort the vanity score for each influencer, as well as to demonstrate understanding of class objects and testing concepts in Python.

## 💻 Tech Stack
The primary technologies used in this project are Python (specifically version 3.9) and the unittest library for writing tests. The choice of these technologies was based on their simplicity, flexibility, and ease of use, as well as their ability to meet the project's requirements.

## 🏗️ Project Architecture
The project's overall architectural pattern is based on a simple, straightforward approach, with a few key components. The main system components are:
* Main: This component contains the main logic of the program, which includes the vanity_sort() function. It also imports the Influencer class from the influencers module and calls it to create three influencer objects.
* Influencers: This module defines a single class called Influencer that represents an influencer on social media. The class has two attributes, num_selfies and num_bio_links, which keep track of the number of selfies and biography links respectively.
* Tests: This module contains test cases for the program's functionality, including test cases for the vanity_sort() function. It also imports the main component from the main module.

## 🧩 Key Components
The main component of the project contains the logic for calculating the vanity score of each influencer and sorting them by that score. The Influencers module defines a class representing an influencer, which has two attributes to keep track of their selfies and biography links. The Tests module contains test cases for verifying the functionality of the vanity_sort() function.

## 🔀 Implementation Flow
The high-level workflow for this project involves the following steps:
* Create three influencer objects with different properties (num_selfies, num_bio_links).
* Calculate the vanity score for each influencer object.
* Sort the list of influencer objects based on their vanity scores using the built-in sorted() function.

## 🚀 Future Improvements
To optimize or scale this project in the future, some potential enhancements could include adding more features to the Influencers class (e.g., additional attributes for tracking followers, engagement metrics, etc.), creating a user interface to allow users to input and sort influencer data interactively, or implementing a more sophisticated sorting algorithm to take into account other factors that affect an influencer's vanity score (e.g., number of posts with images).

---

*Automatically generated architectural overview*
