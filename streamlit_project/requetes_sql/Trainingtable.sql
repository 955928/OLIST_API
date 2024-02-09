-- Create TrainingDataset
CREATE TABLE IF NOT EXISTS TrainingDataset (
    review_id TEXT PRIMARY KEY,
    order_id TEXT,
    review_score INTERGER,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TEXT,
    review_answer_timestamp TEXT,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TEXT,
    order_approved_at TEXT,
    order_delivered_carrier_date TEXT,
    order_delivered_customer_date TEXT,
    order_estimated_delivery_date TEXT,
    score INTEGER,
    temps_livraison TEXT,
    retard_livraison TEXT,
    produit_recu TEXT,
    PRIMARY KEY (review_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    
);