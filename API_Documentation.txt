# API Documentation
## Overview
This document describes a simple mathematical operation API built with the Express framework. The API provides basic arithmetic functions, including addition, subtraction, multiplication, division, and factorial.

## Basic Information
- **API Server Address**: `http://localhost:3000`
- **Port Number**: `3000`
- **Supported HTTP Method**: `GET`
## Features List
### Addition Operation
- **Endpoint**: `/add/:num1/:num2`
- **Description**: Calculates the sum of two numbers.
- **Parameters**:
  - `num1`: The first addend.
  - `num2`: The second addend.
- **Returns**: The sum of the two numbers.

### Subtraction Operation
- **Endpoint**: `/subtract/:num1/:num2`
- **Description**: Calculates the difference between two numbers.
- **Parameters**:
  - `num1`: The minuend.
  - `num2`: The subtrahend.
- **Returns**: The difference between the two numbers.

### Multiplication Operation
- **Endpoint**: `/multiply/:num1/:num2`
- **Description**: Calculates the product of two numbers.
- **Parameters**:
  - `num1`: The first factor.
  - `num2`: The second factor.
- **Returns**: The product of the two numbers.

### Division Operation
- **Endpoint**: `/divide/:num1/:num2`
- **Description**: Calculates the quotient of two numbers.
- **Parameters**:
  - `num1`: The dividend.
  - `num2`: The divisor.
- **Returns**: The quotient of the two numbers.
- **Error Handling**: If the divisor is zero, returns the error message `Cannot divide by zero.`

### Factorial Operation
- **Endpoint**: `/factorial/:num`
- **Description**: Calculates the factorial of a non-negative integer.
- **Parameters**:
  - `num`: The non-negative integer for which the factorial is to be calculated.
- **Returns**: The factorial of the integer.
- **Error Handling**: If the input integer is negative, returns the error message `Factorial of a negative number is undefined.`

## Usage Examples
Below are examples of how to call the API using the cURL command-line tool:

- **Addition**:
  ```bash
  curl http://localhost:3000/add/5/3
  ```

- **Subtraction**:
  ```bash
  curl http://localhost:3000/subtract/10/4
  ```

- **Multiplication**:
  ```bash
  curl http://localhost:3000/multiply/4/5
  ```

- **Division**:
  ```bash
  curl http://localhost:3000/divide/20/5
  ```

- **Factorial**:
  ```bash
  curl http://localhost:3000/factorial/5
  ```