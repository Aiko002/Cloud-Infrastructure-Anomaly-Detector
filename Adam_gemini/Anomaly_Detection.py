import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("your_model_path")

# Make predictions on the test data
predictions = model.predict(test_data[["hour", "day_of_week", "day_of_month", "month", "year"]])

# Calculate anomaly scores (e.g., using reconstruction error)
anomaly_scores = tf.keras.losses.mean_squared_error(test_data["value"], predictions)