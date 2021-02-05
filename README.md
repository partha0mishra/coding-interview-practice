# coding-interview-practice

Enclosed in this repository, are some of the coding interview problems that I have been solving for practice.
<br><br>
The cringe_worthy_practice_problems contains older solutions, some of which are indeed cringe worthy.
<br><br>
Below is a table of leetcode posts which are more recent, however posts between 05/2020 and 09/2020 are also cringe worthy.
<br><br>
The problem number links to the actual problem and the solution links to my posted solution.
<br><br>
About 10% of the problems require a membership to view, the rest do not.
<br>

# solution-types

Arrays, Binary Search, Binary Search Trees (BST), Binary Trees, Bit Manipulation, Breadth First Search (BFS), Change of Base, Depth First Search (DFS), Design Data Structure, Divide and Conquer, Double Ended Queues, Dynamic Programming, Encoding and Decoding, Eulerian Path, Fenwick Trees, Floyd-Warshall, Game Related, Greater Trees, Greedy, Greedy Algorithm, Hashing, Heap, Interval Scheduling, Linked-Lists, Lowest Common Ancestor, Masks, Memoization, Multiset, MySQL, N-ary Trees, Other, Parsing, Path Finding, Pointers, Prefix Sum Array, Probability, Rabin-Karp, Recursion, Scheduling, Segment Tree, Simulation, Skip List, Sliding Window, Sorting, Stacks, State Machines, String Manipulation, Sub-problem, Threading, Top Down DP, Trie, Two-pointer, Union-Find, Visual Solutions

# LeetCode-posts


<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
</script>
    
</head>
<body>

  <br>


<div class="center">
    <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..">
    <input id="myInput" type="text" placeholder="Search.." class="center" size="32">
</div>
<br>
    
<table class="center">
    <colgroup>
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 55%;">
       <col span="1" style="width: 35%;">
    </colgroup>

<table class="center">
<thead>
	<tr>
		<th>Problem</th>
		<th>Solution</th>
		<th>Type</th>
	</tr>
</thead>
<tbody id="myTable">
	<tr>
		<td><a href="https://leetcode.com/problems/longest-palindromic-substring" target="_blank">5</a></td>
		<td><a href="https://leetcode.com/problems/longest-palindromic-substring/discuss/838848/www.youtube.com/www.youtube.com/watch?v=nbTSfrEfo6M" target="_blank">longest palindromic substring</a></td>
		<td>Binary Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/3sum" target="_blank">15</a></td>
		<td><a href="https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated" target="_blank">3sum</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/4sum" target="_blank">18</a></td>
		<td><a href="https://leetcode.com/problems/4sum/discuss/637633/Python-12-Lines-of-Code-168-ms-Annotated" target="_blank">4sum</a></td>
		<td>Pointers</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/valid-parentheses" target="_blank">20</a></td>
		<td><a href="https://leetcode.com/problems/valid-parentheses/discuss/634483/Python-8-Lines-Brief-Explanation" target="_blank">valid parentheses</a></td>
		<td>Stacks</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/reverse-nodes-in-k-group" target="_blank">25</a></td>
		<td><a href="https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/637891/Python-48-ms-Iterative-Approach-with-Comments" target="_blank">reverse nodes in k group</a></td>
		<td>Linked-Lists</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/longest-valid-parentheses" target="_blank">32</a></td>
		<td><a href="https://leetcode.com/problems/longest-valid-parentheses/discuss/638204/Python-a-logical-very-simple-approach-without-a-stack" target="_blank">longest valid parentheses</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/n-queens" target="_blank">51</a></td>
		<td><a href="https://leetcode.com/problems/n-queens/discuss/815397/Python-DFS-with-Bit-Masks" target="_blank">n queens</a></td>
		<td>Depth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/maximal-rectangle" target="_blank">85</a></td>
		<td><a href="https://leetcode.com/problems/maximal-rectangle/discuss/836988/Python-Stack-Solution-with-walk-through-example" target="_blank">maximal rectangle</a></td>
		<td>Stacks</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/pascals-triangle" target="_blank">118</a></td>
		<td><a href="https://leetcode.com/problems/pascals-triangle/discuss/634470/Python-Annotated-Solution" target="_blank">pascals triangle</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/surrounded-regions" target="_blank">130</a></td>
		<td><a href="https://leetcode.com/problems/surrounded-regions/discuss/683921/Python-Recursive-Exploration-Explained" target="_blank">surrounded regions</a></td>
		<td>Recursion</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/palindrome-partitioning" target="_blank">131</a></td>
		<td><a href="https://leetcode.com/problems/palindrome-partitioning/discuss/677585/Python-Simple-Approach-Detailed-Explanation" target="_blank">palindrome partitioning</a></td>
		<td>Recursion</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/word-break" target="_blank">139</a></td>
		<td><a href="https://leetcode.com/problems/word-break/discuss/679805/Python-32-ms-(92)-5-Interesting-Optimizations-Recursive-Solution" target="_blank">word break</a></td>
		<td>Recursion</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/word-break-ii" target="_blank">140</a></td>
		<td><a href="https://leetcode.com/problems/word-break-ii/discuss/631279/Python-98.7-Speed-Simple-Rules-Recursion-Detailed-Comments" target="_blank">word break ii</a></td>
		<td>Recursion</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/one-edit-distance" target="_blank">161</a></td>
		<td><a href="https://leetcode.com/problems/one-edit-distance/discuss/768369/Python-4-Steps-Beats-99.92" target="_blank">one edit distance</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/factorial-trailing-zeroes" target="_blank">172</a></td>
		<td><a href="https://leetcode.com/problems/factorial-trailing-zeroes/discuss/625300/Simple-Python-code-with-a-visual-hint" target="_blank">factorial trailing zeroes</a></td>
		<td>Visual Solutions</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/reverse-words-in-a-string-ii" target="_blank">186</a></td>
		<td><a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/discuss/750135/Python-1-Line-beats-99.6" target="_blank">reverse words in a string ii</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv" target="_blank">188</a></td>
		<td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/782705/Python-Flexible-State-Machine" target="_blank">best time to buy and sell stock iv</a></td>
		<td>State Machines</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/contains-duplicate-iii" target="_blank">220</a></td>
		<td><a href="https://leetcode.com/problems/contains-duplicate-iii/discuss/825392/Python-Simple-Deque-Approach" target="_blank">contains duplicate iii</a></td>
		<td>Sorting</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/contains-duplicate-iii" target="_blank">220</a></td>
		<td><a href="https://leetcode.com/problems/contains-duplicate-iii/discuss/825392/Python-Simple-Deque-Approach" target="_blank">contains duplicate iii</a></td>
		<td>Sorting, Deques</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/paint-house-ii" target="_blank">265</a></td>
		<td><a href="https://leetcode.com/problems/paint-house-ii/discuss/827769/Python-State-Machine-3-Steps" target="_blank">paint house ii</a></td>
		<td>State Machines</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/missing-number" target="_blank">268</a></td>
		<td><a href="https://leetcode.com/problems/missing-number/discuss/634505/Python-One-Line-Solution" target="_blank">missing number</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/integer-to-english-words" target="_blank">273</a></td>
		<td><a href="https://leetcode.com/problems/integer-to-english-words/discuss/797515/Python-Divide-and-Conquer-Three-Steps" target="_blank">integer to english words</a></td>
		<td>Divide and Conquer</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/h-index-ii" target="_blank">275</a></td>
		<td><a href="https://leetcode.com/problems/h-index-ii/discuss/769579/Python-Two-Approaches-Explained-Beats-99.19" target="_blank">h index ii</a></td>
		<td>Binary Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/best-meeting-point" target="_blank">296</a></td>
		<td><a href="https://leetcode.com/problems/best-meeting-point/discuss/826950/Python-Greedy-Exploration-3-Easy-Steps" target="_blank">best meeting point</a></td>
		<td>Greedy Algorithm</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/best-meeting-point" target="_blank">296</a></td>
		<td><a href="https://leetcode.com/problems/best-meeting-point/discuss/826950/Python-Greedy-Exploration-3-Easy-Steps" target="_blank">best meeting point</a></td>
		<td>Greedy Algorithm, Greedy</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/additive-number" target="_blank">306</a></td>
		<td><a href="https://leetcode.com/problems/additive-number/discuss/770231/Python-Simple-Approach-Beats-98.79" target="_blank">additive number</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/range-sum-query-mutable" target="_blank">307</a></td>
		<td><a href="https://leetcode.com/problems/range-sum-query-mutable/discuss/848476/Python-Fenwick-Tree-with-resources" target="_blank">range sum query mutable</a></td>
		<td>Fenwick Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/range-sum-query-2d-mutable" target="_blank">308</a></td>
		<td><a href="https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/848528/Python-Fenwick-Tree-%2B-Memoization-with-resources" target="_blank">range sum query 2d mutable</a></td>
		<td>Fenwick Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/bulb-switcher" target="_blank">319</a></td>
		<td><a href="https://leetcode.com/problems/bulb-switcher/discuss/770172/Python-Steps-to-Reach-Solution-with-Visual-Aid" target="_blank">bulb switcher</a></td>
		<td>Visual Solutions</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/design-tic-tac-toe" target="_blank">348</a></td>
		<td><a href="https://leetcode.com/problems/design-tic-tac-toe/discuss/677685/Python-Beats-98.63-Simple-Approach-Explained" target="_blank">design tic tac toe</a></td>
		<td>Game Related</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii" target="_blank">350</a></td>
		<td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/634072/Python-99.85-Fastest-light-comments" target="_blank">intersection of two arrays ii</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters" target="_blank">395</a></td>
		<td><a href="https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/679442/Python-36-ms-Recursion-and-Counter-Explained" target="_blank">longest substring with at least k repeating characters</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/rotate-function" target="_blank">396</a></td>
		<td><a href="https://leetcode.com/problems/rotate-function/discuss/837477/Python-Simple-Example" target="_blank">rotate function</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/evaluate-division" target="_blank">399</a></td>
		<td><a href="https://leetcode.com/problems/evaluate-division/discuss/706819/Python-find-path-from-a-to-b-annotated" target="_blank">evaluate division</a></td>
		<td>Path Finding</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list" target="_blank">430</a></td>
		<td><a href="https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/633880/Python-Simple-While-Loop-83-Speed" target="_blank">flatten a multilevel doubly linked list</a></td>
		<td>Linked-Lists</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array" target="_blank">448</a></td>
		<td><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/632746/Python-98.4-Speed-5-lines (this may belong in other)" target="_blank">find all numbers disappeared in an array</a></td>
		<td>Masks</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/island-perimeter" target="_blank">463</a></td>
		<td><a href="https://leetcode.com/problems/island-perimeter/discuss/651915/Python-Land-and-Expand-A-Recursive-Approach-Explained" target="_blank">island perimeter</a></td>
		<td>Recursion</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/ones-and-zeroes" target="_blank">474</a></td>
		<td><a href="https://leetcode.com/problems/ones-and-zeroes/discuss/837125/Python-Memoization-3-Steps" target="_blank">ones and zeroes</a></td>
		<td>Memoization</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/diagonal-traverse" target="_blank">498</a></td>
		<td><a href="https://leetcode.com/problems/diagonal-traverse/discuss/711058/Python-11-lines-Easy-Way-to-Visualize-a-Solution" target="_blank">diagonal traverse</a></td>
		<td>Visual Solutions</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/next-greater-element-ii" target="_blank">503</a></td>
		<td><a href="https://leetcode.com/problems/next-greater-element-ii/discuss/825924/Python-Simple-Stack-Approach-5-Steps" target="_blank">next greater element ii</a></td>
		<td>Stacks</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/base-7" target="_blank">504</a></td>
		<td><a href="https://leetcode.com/problems/base-7/discuss/672274/Python-Short-and-Simple-with-Explanation-and-Resources (consider moving this to stacks)" target="_blank">base 7</a></td>
		<td>Change of Base</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/most-frequent-subtree-sum" target="_blank">508</a></td>
		<td><a href="https://leetcode.com/problems/most-frequent-subtree-sum/discuss/788093/Python-Post-Order-Traverse-Annotated-Beats-99" target="_blank">most frequent subtree sum</a></td>
		<td>Binary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/inorder-successor-in-bst-ii" target="_blank">510</a></td>
		<td><a href="https://leetcode.com/problems/inorder-successor-in-bst-ii/discuss/771281/Python-Clean-and-Short-Explained" target="_blank">inorder successor in bst ii</a></td>
		<td>Binary Search Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minesweeper" target="_blank">529</a></td>
		<td><a href="https://leetcode.com/problems/minesweeper/discuss/710808/Python-annotated-easy-to-read" target="_blank">minesweeper</a></td>
		<td>Game Related</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/convert-bst-to-greater-tree" target="_blank">538</a></td>
		<td><a href="https://leetcode.com/problems/convert-bst-to-greater-tree/discuss/662081/Python-Faster-than-100-Explained" target="_blank">convert bst to greater tree</a></td>
		<td>Greater Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/friend-circles" target="_blank">547</a></td>
		<td><a href="https://leetcode.com/problems/friend-circles/discuss/778619/Python-Alternative-to-Union-Find-Beats-100" target="_blank">friend circles</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/reverse-words-in-a-string-iii" target="_blank">557</a></td>
		<td><a href="https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/639753/Python-Two-1-Line-Solutions-Explained" target="_blank">reverse words in a string iii</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/maximum-vacation-days" target="_blank">568</a></td>
		<td><a href="https://leetcode.com/problems/maximum-vacation-days/discuss/843675/Python-BFS-with-Optimization-Beats-97" target="_blank">maximum vacation days</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/squirrel-simulation" target="_blank">573</a></td>
		<td><a href="https://leetcode.com/problems/squirrel-simulation/discuss/825959/Python-Simple-Approach-Rephrased-Question" target="_blank">squirrel simulation</a></td>
		<td>Path Finding</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/design-compressed-string-iterator" target="_blank">604</a></td>
		<td><a href="https://leetcode.com/problems/design-compressed-string-iterator/discuss/674097/Python-Memory-Error-Solution-2-Stacks-and-Detailed-Explanation" target="_blank">design compressed string iterator</a></td>
		<td>Stacks</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/add-bold-tag-in-string" target="_blank">616</a></td>
		<td><a href="https://leetcode.com/problems/add-bold-tag-in-string/discuss/764133/Python-3-Steps-Rabin-Karp-Merge-Intervals-Add-Tags" target="_blank">add bold tag in string</a></td>
		<td>Rabin-Karp</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/maximum-length-of-pair-chain" target="_blank">646</a></td>
		<td><a href="https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/791780/Python-Greedy-6-Lines-Explained" target="_blank">maximum length of pair chain</a></td>
		<td>Sorting</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/2-keys-keyboard" target="_blank">650</a></td>
		<td><a href="https://leetcode.com/problems/2-keys-keyboard/discuss/786906/python-the-intuitive-way-not-mathy" target="_blank">2 keys keyboard</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/partition-to-k-equal-sum-subsets" target="_blank">698</a></td>
		<td><a href="https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/817767/Python-3-steps-DFS-with-bit-masks" target="_blank">partition to k equal sum subsets</a></td>
		<td>Depth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list" target="_blank">708</a></td>
		<td><a href="https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/discuss/690630/Python-32-ms-with-detailed-annotations" target="_blank">insert into a sorted circular linked list</a></td>
		<td>Linked-Lists</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-distinct-islands-ii" target="_blank">711</a></td>
		<td><a href="https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/790616/Python-3-Steps-Group-Transform-Find-Duplicates" target="_blank">number of distinct islands ii</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/maximum-length-of-repeated-subarray" target="_blank">718</a></td>
		<td><a href="https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/843718/Python-Binary-Search-2-Steps" target="_blank">maximum length of repeated subarray</a></td>
		<td>Binary Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/accounts-merge" target="_blank">721</a></td>
		<td><a href="https://leetcode.com/problems/accounts-merge/discuss/778528/Python-Alternative-to-Union-Find-Beats-99-Annotated" target="_blank">accounts merge</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sentence-similarity-ii" target="_blank">737</a></td>
		<td><a href="https://leetcode.com/problems/sentence-similarity-ii/discuss/784419/Python-Alternative-to-Union-Find-Beats-100" target="_blank">sentence similarity ii</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/prefix-and-suffix-search" target="_blank">745</a></td>
		<td><a href="https://leetcode.com/problems/prefix-and-suffix-search/discuss/788550/Python-Trie-with-clarifications-and-tips" target="_blank">prefix and suffix search</a></td>
		<td>Trie</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-corner-rectangles" target="_blank">750</a></td>
		<td><a href="https://leetcode.com/problems/number-of-corner-rectangles/discuss/693174/Python-Beats-99.4-10-Lines-Three-Steps-Explained" target="_blank">number of corner rectangles</a></td>
		<td>Arrays</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/open-the-lock" target="_blank">752</a></td>
		<td><a href="https://leetcode.com/problems/open-the-lock/discuss/702332/Python-216-ms-(95)-BFS-with-Optimizations-Detailed-Explanation" target="_blank">open the lock</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/set-intersection-size-at-least-two" target="_blank">757</a></td>
		<td><a href="https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/795641/Python-Greedy-Approach-Annotated" target="_blank">set intersection size at least two</a></td>
		<td>Sorting</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/find-anagram-mappings" target="_blank">760</a></td>
		<td><a href="https://leetcode.com/problems/find-anagram-mappings/discuss/650194/Python-beats-99.71-5-Lines-Explained" target="_blank">find anagram mappings</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sliding-puzzle" target="_blank">773</a></td>
		<td><a href="https://leetcode.com/problems/sliding-puzzle/discuss/842133/python-rabin-karp-with-bfs" target="_blank">sliding puzzle</a></td>
		<td>Rabin-Karp</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sliding-puzzle" target="_blank">773</a></td>
		<td><a href="https://leetcode.com/problems/sliding-puzzle/discuss/842133/python-rabin-karp-with-bfs" target="_blank">sliding puzzle</a></td>
		<td>Rabin-Karp, Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/similar-rgb-color" target="_blank">800</a></td>
		<td><a href="https://leetcode.com/problems/similar-rgb-color/discuss/652574/Python-3-Step-Solution-Explained" target="_blank">similar rgb color</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/subdomain-visit-count" target="_blank">811</a></td>
		<td><a href="https://leetcode.com/problems/subdomain-visit-count/discuss/639733/Python-8-Lines-48-ms-Beats-93" target="_blank">subdomain visit count</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/binary-tree-pruning" target="_blank">814</a></td>
		<td><a href="https://leetcode.com/problems/binary-tree-pruning/discuss/688847/Python-28-ms-Post-Order-Leaf-Trimmer-Explained" target="_blank">binary tree pruning</a></td>
		<td>Binary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/race-car" target="_blank">818</a></td>
		<td><a href="https://leetcode.com/problems/race-car/discuss/762584/Python-3-Simple-Steps-(BFS)" target="_blank">race car</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/short-encoding-of-words" target="_blank">820</a></td>
		<td><a href="https://leetcode.com/problems/short-encoding-of-words/discuss/763857/Python-2-Trie-Solutions-Explained" target="_blank">short encoding of words</a></td>
		<td>Trie</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/shortest-distance-to-a-character" target="_blank">821</a></td>
		<td><a href="https://leetcode.com/problems/shortest-distance-to-a-character/discuss/635954/Python-Two-Passes-of-S-(36-ms)-Explained" target="_blank">shortest distance to a character</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/goat-latin" target="_blank">824</a></td>
		<td><a href="https://leetcode.com/problems/goat-latin/discuss/652229/Python-Straight-Forward-Solution-Detailed-Annotations" target="_blank">goat latin</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/similar-string-groups" target="_blank">839</a></td>
		<td><a href="https://leetcode.com/problems/similar-string-groups/discuss/785096/python-accepted-solution-annotated" target="_blank">similar string groups</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/similar-string-groups" target="_blank">839</a></td>
		<td><a href="https://leetcode.com/problems/similar-string-groups/discuss/785096/python-accepted-solution-annotated" target="_blank">similar string groups</a></td>
		<td>Group by ID (Union-Find Alternative), Trie</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/buddy-strings" target="_blank">859</a></td>
		<td><a href="https://leetcode.com/problems/buddy-strings/discuss/686783/Python-28-ms-(91)-9-lines-simple-explanation" target="_blank">buddy strings</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/uncommon-words-from-two-sentences" target="_blank">884</a></td>
		<td><a href="https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/652246/Python-Aesthetically-Pleasing-2-Line-Solution-Explained" target="_blank">uncommon words from two sentences</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/super-egg-drop" target="_blank">887</a></td>
		<td><a href="https://leetcode.com/problems/super-egg-drop/discuss/746972/Python-5-Lines-with-Video-Link-beats-95" target="_blank">super egg drop</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/groups-of-special-equivalent-strings" target="_blank">893</a></td>
		<td><a href="https://leetcode.com/problems/groups-of-special-equivalent-strings/discuss/641006/Python-1-Liner-and-5-Liner-(for-readability)-Explained" target="_blank">groups of special equivalent strings</a></td>
		<td>Hashing</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/smallest-range-i" target="_blank">908</a></td>
		<td><a href="https://leetcode.com/problems/smallest-range-i/discuss/641033/Python-Explained-Question-Simple-Solution-Bonus-1-Liner" target="_blank">smallest range i</a></td>
		<td>Arrays</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/snakes-and-ladders" target="_blank">909</a></td>
		<td><a href="https://leetcode.com/problems/snakes-and-ladders/discuss/737052/Python-Step-1-Unravel-to-1D-Array-Step-2-Search" target="_blank">snakes and ladders</a></td>
		<td>Game Related</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sort-array-by-parity-ii" target="_blank">922</a></td>
		<td><a href="https://leetcode.com/problems/sort-array-by-parity-ii/discuss/639861/Python-3-Methods" target="_blank">sort array by parity ii</a></td>
		<td>Arrays</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimize-malware-spread" target="_blank">924</a></td>
		<td><a href="https://leetcode.com/problems/minimize-malware-spread/discuss/784530/Python-Alternative-to-Union-Find-3-Steps-Beats-98.7" target="_blank">minimize malware spread</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimize-malware-spread-ii" target="_blank">928</a></td>
		<td><a href="https://leetcode.com/problems/minimize-malware-spread-ii/discuss/784601/Python-4-Steps-Alternative-to-Union-Find" target="_blank">minimize malware spread ii</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-recent-calls" target="_blank">933</a></td>
		<td><a href="https://leetcode.com/problems/number-of-recent-calls/discuss/636175/Python-Simple-Solution-Quick-Explanation" target="_blank">number of recent calls</a></td>
		<td>Design Data Structure</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/reveal-cards-in-increasing-order" target="_blank">950</a></td>
		<td><a href="https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/689019/Python-44-ms-Explained" target="_blank">reveal cards in increasing order</a></td>
		<td>Game Related</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/regions-cut-by-slashes" target="_blank">959</a></td>
		<td><a href="https://leetcode.com/problems/regions-cut-by-slashes/discuss/786478/python-visual-explanation" target="_blank">regions cut by slashes</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/regions-cut-by-slashes" target="_blank">959</a></td>
		<td><a href="https://leetcode.com/problems/regions-cut-by-slashes/discuss/786478/python-visual-explanation" target="_blank">regions cut by slashes</a></td>
		<td>Group by ID (Union-Find Alternative), Visual Solutions</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-area-rectangle-ii" target="_blank">963</a></td>
		<td><a href="https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/760954/Python-Using-Vectors-Sketches-and-Explanation-Included" target="_blank">minimum area rectangle ii</a></td>
		<td>Visual Solutions</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/satisfiability-of-equality-equations" target="_blank">990</a></td>
		<td><a href="https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/784473/Python-3-Steps-Alternative-to-Union-Find-Beats-99" target="_blank">satisfiability of equality equations</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips" target="_blank">995</a></td>
		<td><a href="https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/846869/Python-Greedy-Queue" target="_blank">minimum number of k consecutive bit flips</a></td>
		<td>Greedy</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/grid-illumination" target="_blank">1001</a></td>
		<td><a href="https://leetcode.com/problems/grid-illumination/discuss/815338/Python-Making-a-Hard-Problem-Easy-Beats-100-Annotated" target="_blank">grid illumination</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-enclaves" target="_blank">1020</a></td>
		<td><a href="https://leetcode.com/problems/number-of-enclaves/discuss/790257/3-Solutions-BFS-DFS-and-Union-Find" target="_blank">number of enclaves</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-enclaves" target="_blank">1020</a></td>
		<td><a href="https://leetcode.com/problems/number-of-enclaves/discuss/790257/3-Solutions-BFS-DFS-and-Union-Find" target="_blank">number of enclaves</a></td>
		<td>Breadth First Search, Depth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers" target="_blank">1022</a></td>
		<td><a href="https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/640967/Python-2-Recursive-Methods" target="_blank">sum of root to leaf binary numbers</a></td>
		<td>Binary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/escape-a-large-maze" target="_blank">1036</a></td>
		<td><a href="https://leetcode.com/problems/escape-a-large-maze/discuss/773637/Python-BFS-from-both-ends-with-Escape-Condition" target="_blank">escape a large maze</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/lexicographically-smallest-equivalent-string" target="_blank">1061</a></td>
		<td><a href="https://leetcode.com/problems/lexicographically-smallest-equivalent-string/discuss/776792/Python-Group-by-ID-Beats-100-Runtime-and-Memory" target="_blank">lexicographically smallest equivalent string</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths" target="_blank">1080</a></td>
		<td><a href="https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/discuss/788775/Python-Sum-Paths-then-Trim-Paths-Annoated" target="_blank">insufficient nodes in root to leaf paths</a></td>
		<td>Binary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/largest-values-from-labels" target="_blank">1090</a></td>
		<td><a href="https://leetcode.com/problems/largest-values-from-labels/discuss/828706/Python-Greedy-3-Simple-Steps-Explained" target="_blank">largest values from labels</a></td>
		<td>Greedy</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters" target="_blank">1100</a></td>
		<td><a href="https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/691501/Python-40-ms-(96)-counting-window-explained" target="_blank">find k length substrings with no repeated characters</a></td>
		<td>Sliding Window</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/parsing-a-boolean-expression" target="_blank">1106</a></td>
		<td><a href="https://leetcode.com/problems/parsing-a-boolean-expression/discuss/829137/Python-2-Stacks-O(n)-Solution" target="_blank">parsing a boolean expression</a></td>
		<td>Stacks</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/parsing-a-boolean-expression" target="_blank">1106</a></td>
		<td><a href="https://leetcode.com/problems/parsing-a-boolean-expression/discuss/829137/Python-2-Stacks-O(n)-Solution" target="_blank">parsing a boolean expression</a></td>
		<td>Stacks, Parsing</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/alphabet-board-path" target="_blank">1138</a></td>
		<td><a href="https://leetcode.com/problems/alphabet-board-path/discuss/788138/Python-Clean-and-Annotated-Easy-to-Understand" target="_blank">alphabet board path</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/online-majority-element-in-subarray" target="_blank">1157</a></td>
		<td><a href="https://leetcode.com/problems/online-majority-element-in-subarray/discuss/729311/Python-Segment-Tree-Annotated" target="_blank">online majority element in subarray</a></td>
		<td>Segment Tree</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations" target="_blank">1210</a></td>
		<td><a href="https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/discuss/736930/Python-BFS-Annotated" target="_blank">minimum moves to reach target with rotations</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations" target="_blank">1210</a></td>
		<td><a href="https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/discuss/736930/Python-BFS-Annotated" target="_blank">minimum moves to reach target with rotations</a></td>
		<td>Breadth First Search, Game Related</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position" target="_blank">1217</a></td>
		<td><a href="https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/discuss/650808/Python-Detailed-Explanation-and-Concise-2-Line-Solution" target="_blank">minimum cost to move chips to the same position</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/path-with-maximum-gold" target="_blank">1219</a></td>
		<td><a href="https://leetcode.com/problems/path-with-maximum-gold/discuss/776747/Python-BFS-beats-97" target="_blank">path with maximum gold</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/remove-sub-folders-from-the-filesystem" target="_blank">1233</a></td>
		<td><a href="https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/829101/Python-Simple-Trie-4-Steps" target="_blank">remove sub folders from the filesystem</a></td>
		<td>Trie</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/web-crawler" target="_blank">1236</a></td>
		<td><a href="https://leetcode.com/problems/web-crawler/discuss/776875/Python-Short-and-Simple-DFS-beats-97.7" target="_blank">web crawler</a></td>
		<td>String Manipulation</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/smallest-common-region" target="_blank">1257</a></td>
		<td><a href="https://leetcode.com/problems/smallest-common-region/discuss/778594/Python-4-Steps-Clean-and-Annotated" target="_blank">smallest common region</a></td>
		<td>Lowest Common Ancestor</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/smallest-common-region" target="_blank">1257</a></td>
		<td><a href="https://leetcode.com/problems/smallest-common-region/discuss/778594/Python-4-Steps-Clean-and-Annotated" target="_blank">smallest common region</a></td>
		<td>Lowest Common Ancestor, N-ary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends" target="_blank">1258</a></td>
		<td><a href="https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/discuss/776624/Python-Pretend-Islands-4-Steps" target="_blank">the earliest moment when everyone become friends</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends" target="_blank">1258</a></td>
		<td><a href="https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/discuss/776624/Python-Pretend-Islands-4-Steps" target="_blank">the earliest moment when everyone become friends</a></td>
		<td>Group by ID (Union-Find Alternative), Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-time-visiting-all-points" target="_blank">1266</a></td>
		<td><a href="https://leetcode.com/problems/minimum-time-visiting-all-points/discuss/638347/Python-Simple-Walk-Through" target="_blank">minimum time visiting all points</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix" target="_blank">1284</a></td>
		<td><a href="https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/discuss/841955/Python-BFS-two-important-observations" target="_blank">minimum number of flips to convert binary matrix to zero matrix</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array" target="_blank">1287</a></td>
		<td><a href="https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/659328/Python-Simple-4-Liner-Explained" target="_blank">element appearing more than 25 in sorted array</a></td>
		<td>Two-pointer</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer" target="_blank">1290</a></td>
		<td><a href="https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/638277/Python-2-Solutions-(24-ms)-Detailed-Explanations" target="_blank">convert binary number in a linked list to integer</a></td>
		<td>Linked-Lists</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sequential-digits" target="_blank">1291</a></td>
		<td><a href="https://leetcode.com/problems/sequential-digits/discuss/815416/Python-Two-Step-Solution" target="_blank">sequential digits</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/distinct-echo-substrings" target="_blank">1316</a></td>
		<td><a href="https://leetcode.com/problems/distinct-echo-substrings/discuss/831379/python-presum-hash-sliding-window-beats-100-14-lines" target="_blank">distinct echo substrings</a></td>
		<td>Rabin-Karp</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-operations-to-make-network-connected" target="_blank">1319</a></td>
		<td><a href="https://leetcode.com/problems/number-of-operations-to-make-network-connected/discuss/783070/Python-Alternative-to-Union-Find-Beats-100" target="_blank">number of operations to make network connected</a></td>
		<td>Group by ID (Union-Find Alternative)</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/maximum-students-taking-exam" target="_blank">1349</a></td>
		<td><a href="https://leetcode.com/problems/maximum-students-taking-exam/discuss/833729/Python-Greedy-Graph-3-Steps" target="_blank">maximum students taking exam</a></td>
		<td>Greedy Algorithm</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix" target="_blank">1351</a></td>
		<td><a href="https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/639451/Python-Beats-92-9-Lines-Explained" target="_blank">count negative numbers in a sorted matrix</a></td>
		<td>Visual Solutions</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits" target="_blank">1356</a></td>
		<td><a href="https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/discuss/639844/Python-2-Methods-With-and-Without-bin" target="_blank">sort integers by the number of 1 bits</a></td>
		<td>Sorting</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/number-of-days-between-two-dates" target="_blank">1360</a></td>
		<td><a href="https://leetcode.com/problems/number-of-days-between-two-dates/discuss/703030/Python-beats-95-clean-and-annotated" target="_blank">number of days between two dates</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid" target="_blank">1368</a></td>
		<td><a href="https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/discuss/843595/Python-BFS-short-and-annotated" target="_blank">minimum cost to make at least one valid path in a grid</a></td>
		<td>Breadth First Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/frog-position-after-t-seconds" target="_blank">1377</a></td>
		<td><a href="https://leetcode.com/problems/frog-position-after-t-seconds/discuss/788811/python-frog-army-with-notes" target="_blank">frog position after t seconds</a></td>
		<td>Probability</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree" target="_blank">1379</a></td>
		<td><a href="https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/discuss/684192/Python-640-ms-(99)-Explained" target="_blank">find a corresponding node of a binary tree in a clone of that tree</a></td>
		<td>Binary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/find-the-distance-value-between-two-arrays" target="_blank">1385</a></td>
		<td><a href="https://leetcode.com/problems/find-the-distance-value-between-two-arrays/discuss/640002/Python-Short-and-Simple" target="_blank">find the distance value between two arrays</a></td>
		<td>Arrays</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/leftmost-column-with-at-least-a-one" target="_blank">1428</a></td>
		<td><a href="https://leetcode.com/problems/leftmost-column-with-at-least-a-one/discuss/699078/Python-beats-99.8-binary-search-approach-explained" target="_blank">leftmost column with at least a one</a></td>
		<td>Binary Search</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree" target="_blank">1430</a></td>
		<td><a href="https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/discuss/698077/Python-beats-99.8-annotated-and-explained" target="_blank">check if a string is a valid sequence from root to leaves path in a binary tree</a></td>
		<td>Binary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/build-an-array-with-stack-operations" target="_blank">1441</a></td>
		<td><a href="https://leetcode.com/problems/build-an-array-with-stack-operations/discuss/636211/Python-98.6-Speed-8-lines" target="_blank">build an array with stack operations</a></td>
		<td>Arrays</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence" target="_blank">1455</a></td>
		<td><a href="https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/discuss/649890/Python-Short-and-Simple-28ms-(100-speed-and-memory)" target="_blank">check if a word occurs as a prefix of any word in a sentence</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/avoid-flood-in-the-city" target="_blank">1488</a></td>
		<td><a href="https://leetcode.com/problems/avoid-flood-in-the-city/discuss/838640/Python-Save-it-for-a-rainy-day..." target="_blank">avoid flood in the city</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/clone-n-ary-tree" target="_blank">1490</a></td>
		<td><a href="https://leetcode.com/problems/clone-n-ary-tree/discuss/711862/Python-with-short-explanation" target="_blank">clone n ary tree</a></td>
		<td>N-ary Trees</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank" target="_blank">1503</a></td>
		<td><a href="https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/discuss/720237/Python-One-line-solution-with-explanation" target="_blank">last moment before all ants fall out of a plank</a></td>
		<td>Other</td>
	</tr>
	<tr>
		<td><a href="https://leetcode.com/problems/find-root-of-n-ary-tree" target="_blank">1506</a></td>
		<td><a href="https://leetcode.com/problems/find-root-of-n-ary-tree/discuss/731092/Python-Beats-100-2-Approaches-O(N)-Time-and-O(N)O(1)-Space" target="_blank">find root of n ary tree</a></td>
		<td>N-ary Trees</td>
	</tr>
</tbody>
</table>
