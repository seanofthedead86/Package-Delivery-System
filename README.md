# Package-Delivery-System

1.  Explain the algorithm’s logic using pseudocode.
The algorithm being used is a nearest neighbor algorithm. The algorithm looks at your current point and calculates the distance to each other location, finding the shortest distance, and visiting it. It then repeats that over and over, starting from your last point visited until all points have been visited. Prior to starting the algorithm, you establish the queues, the default time, current location, and current lowest distance, a number much greater than would be calculated in the algorithm. 
while the length of queue is > 0
	if a users input time < the current time
		end the algorithm
	for each location in the queue
		find the distance between each location and every other location
		If that distance is less than the default/previous distance
			save that distance as the shortest distance
	Append each distance in the total distance list
	For each package in the list
		Find the address at the current location from the address data
		create a package object using the hash table search function
		create an object for the package address using 'get attribute'
		if the current address matches the package address
			mark the package status as delivered
			calculate time traveled ((current distance / 18) * 18)
			calculate time delivered
			calculate total sum miles from the total distance list
	remove package from the queue 
	
In the program, this algorithm is repeated twice per truck, once for the packages in the priority queue and once for the regular package queue. At the end of the second time the algorithm runs, the distance is calculated back to the start and total time and distance are saved for the truck.  
1.	Describe at least two strengths of the algorithm used in the solution.
The first strength of the algorithm is speed. It has an overall time complex of O(n^2). The second strength is its simplicity of just trying to find the shortest path, regardless of any constraints. 

2.	Verify that the algorithm used in the solution meets all requirements in the scenario.
The algorithm meets all requirements

3.	Identify two other named algorithms, different from the algorithm implemented in the solution that would meet the requirements in the scenario.  

Dijkstra’s algorithm and Greedy Algorithm

a.	Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.
One algorithm that could be used is Dijkstra’s algorithm. Dijkstra’s “determines the shortest path from a start vertex to each vertex in a graph” (“C950: Data Structures and Algorithms” Chapter 6, Section 11). Another algorithm that could be used is the Greedy Algorithm that “solves a problem by assuming that the optimal choice at a given moment during the algorithm will also be the optimal choice overall” (“C950: Data Structures and Algorithms” Chapter 3, Section 4).  The biggest difference between the two algorithms is the Greedy Algorithm assumes that the best choice is the choice in that moment while Dijkstra’s can find the solution using all available outcomes. Simply put, Dijkstra’s looks at the problem has a whole with Greedy does not. This can lead the Greedy algorithm to find a path, but it may to be the shortest. This does, however, lead the Greedy algorithm having a faster output that Dijkstra’s. 

One data structure that could be used would be a graph. “A graph is a data structure for representing connections among items, and consists of vertices connected by edges” (“C950: Data Structures and Algorithms” Chapter 9, Section 4).  Another data that could be used is a nested dictionary, which is a dictionary that “contains another dictionary as a value” (“C950: Data Structures and Algorithms” Chapter 6, Section 1). In the instance of this project, you could have a key as the current location and the value be a dictionary of key-value pairs of destinations and their distance from the current location. A graph could be complicated to implement, especially if it keeps expanding with more and data that needs to be added (i.e. packages with a new address that needs to be delivered to). A nested dictionary tends to be a more streamlined way to represent data, however, it could also be a more time consuming and complicated, as well as more prone to errors. 

2.  Describe the programming environment you used to create the Python application.
Used JetBrains PyCharm IDE Version 2021.2.3 and Replit web based IDE on Windows 10/11
3.  Evaluate the space-time complexity of each major segment of the program, and the entire program, using big-O notation.
Space time complexity of the entire program is O(n^2)
Please see project application code comments for space-time complexity of individual parts of the program
4.  Explain the capability of your solution to scale and adapt to a growing number of packages.
The algorithm is not well suited to being able to scale with an increasing number of packages.  The program is set up with high priority and low priority packages being separated manually. The algorithm doesn’t care if there is a time constraint on a package being delivered, just that it needs to be delivered. It is possible that a package may be delivered late if it ends up in the wrong priority list or on a truck that leaves at a later time. Knowing this, if packages were added to the package CSV, they would need to be looked at and at separated into the correct priority list for the correct truck based on any constraints.  
5.  Discuss why the software is efficient and easy to maintain.
The program uses a very basic algorithm to complete its task. The more packages that will need to be delivered, the slower the program will run. The software also needs the user to manual separate the packages based on constraints for it to meet all expectations. While this doesn’t make the software the most efficient way to complete the task, the algorithm itself is very basic to understand. 
6.  Discuss the strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).
The biggest advantage of a Chaining Hash Table is the insert method is always successful; “ In other hash table implementations, insert() fails when the hash table is full, so chaining has the advantage of not having a limit to how many items can be inserted.” Hash tables also need to be designed to avoid collisions and can be slowed down if there are collisions, which is the primary weakness of a hash table (“C950: Data Structures and Algorithms” Chapter 7, Section 2).
a.	Explain how the time needed to complete the look-up function is affected by changes in the number of packages to be delivered.
The lookup function of hash table’s time would increase as the number of packages increases. The function searches through each entry in the hash function, looking for the corresponding key number. In theory, it could look through every single package in the hash table before finding the correct one if the user was looking up the last entry. In a chaining hash table, this is reduced with multiple items placed in a list per bucket.  

b.	Explain how the data structure space usage is affected by changes in the number of packages to be delivered.
More packages would mean buckets in the hash table become fuller, slowing down the search function.

c.	Describe how changes to the number of trucks or the number of cities would affect the look-up time and the space usage of the data structure.
Changes to the number of trucks or addresses would not affect the search of the hash table because the packages hash table is separate from the addresses and trucks. Increasing the number of trucks would slow down the overall goal of the software if the number of drivers for the trucks doesn’t increase. 
