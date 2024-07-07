## Facility Assignment and Routing Problem: Finding the Optimal Solution

**The Problem:** Given a set of orders, we need to:

1. **Assign Orders to Plants:**  Determine the most suitable plant to process each order considering product restrictions and vendor-managed inventory (VMI) constraints.
2. **Route Orders to Ports:** Select the optimal port for shipping each order based on plant-port connections and freight rates.

**Data & Restrictions:**

* Data includes information on plant-port connections, order details, product-plant compatibility, VMI customers, freight rates, and manufacturing costs.
* Key restrictions:
    * **Product Restrictions:** Plants can only produce certain products.
    * **Port Restrictions:** Plants are only connected to specific ports.
    * **VMI Restrictions:** Some customers require service from a designated plant.

**Approach:**

1. **Data Preparation:** Clean and prepare data, creating a NetworkX graph to represent plant-port connections.
2. **Supply Chain Visualization:** Visualize the network using NetworkX and Plotly for interactive exploration.
3. **Order Processing:** 
    * Exclude orders that can't be processed due to restrictions.
    * Identify the set of plants capable of processing each order.
4. **Order Assignment & Routing:**
    * Aggregate freight rates for each port for simplified cost calculation.
    * Employ functions `min_cost` and `find_best_port` to find the cheapest plant-port combination for each order, considering both manufacturing and freight costs.
    * Assign orders to plants and ports, recording the solution in the "decision" column of the order table.
5. **Visualization:** Plot the number of products each plant manufactures and the manufacturing cost per unit for each plant.

**Key Functions:**

* **`product_restriction(index)`:** Returns possible plants based on product restrictions.
* **`customer_restriction(index)`:** Returns possible plants based on VMI restrictions.
* **`check_order(Order_Id, length=True)`:** Combines product and VMI restrictions to identify feasible plants for an order.
* **`min_cost(dec_space)`:** Finds the cheapest plant-port combination for a given set of possible plants.
* **`find_best_port(plant_id)`:** Determines the best port for shipping from a given plant based on freight rates.

**Web Link**: https://supplychain12.streamlit.app/
