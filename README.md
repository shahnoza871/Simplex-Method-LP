# Optimization via Simplex Method

## Overview
This project implements the **Simplex Method** for solving **Linear Programming (LP) problems** related to **optimization and maximization**. The algorithm finds the optimal solution to a linear objective function subject to linear constraints using an iterative matrix-based approach.

## Features
- Implements the **Simplex Method** for solving **linear programming problems**.
- Reads LP problems from input files and constructs the corresponding **augmented matrix**.
- Handles **greater than (≥)** and **less than (≤)** constraints automatically.
- Identifies **basic and non-basic solutions** during iteration.
- Iteratively transforms the tableau into **reduced row echelon form (RREF)**.
- Supports **multiple iterations** to reach the optimal solution.
- Outputs step-by-step matrix transformations and final optimal solution.

## Prerequisites
Ensure you have the following dependencies installed:

## Usage

### Input File Format
The input file should be structured as follows:
1. Number of variables (n)
2. Number of constraints (m)
3. Coefficients of the objective function (space-separated)
4. Constraint types (`ge`, `le`, or `equal` for `≥`, `≤`, and `=` respectively)
5. Coefficients of constraints, including RHS constant (space-separated)

