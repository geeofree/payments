# Payments

A toy web application for a payments service system.

## System Entities

### Users

The application contains four (4) user types that drives the interaction 
with other entities in the system and are grouped as follows:

#### Management

Management users handle anything thats related to users in the system.

- Master: The master user manages administrator users as well as the 
  system configurations.
- Administrator: Manages *client* users.

#### Client

Client users interact with products and create transactions in the system.

- Biller: Manages products that will be sold to customers.
- Customer: Product consumer.

### Products & Transactions

Billers can create products which are forms that contain fields and also contain prices.

When a customer buys a product a transaction is made.

The application also sets fee rates which affects the calculation of each transaction.

## Technical Overview

TBD: Describe the technical implementation in a high-level manner.
