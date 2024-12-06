# Ensure the predictions table exists
create_predictions_table()

# Load the model
model = load_model_from_keras(args.model_name)

# Load the test data
x_test, _ = load_dataset(args.dataset_name, is_training=False)

 # Predict on the test data
 predictions = model.predict(x_test)
  predicted_labels = np.argmax(predictions, axis=1)

   # Save predictions to the database
   try:
        conn, cursor = create_connection()
        for image_idx, predicted_label in enumerate(predicted_labels):
            query = """
                INSERT INTO image_predictions (id, image_id, predicted_label, model_name, prediction_timestamp)
                VALUES (%s, %s, %s, %s, %s);
                """
            # Generate a new UUID for the prediction
            prediction_id = str(uuid.uuid4())

            # Assuming `image_id` is retrievable; adapt if x_test does not include it
            # Modify if image_id is not directly available
            image_id = x_test[image_idx]
            prediction_timestamp = datetime.now()

            cursor.execute(query, (prediction_id, image_id, str(
                predicted_label), args.model_name, prediction_timestamp))

        conn.commit()
        print("Predictions stored successfully in the database.")
    except Exception as e:
        print(f"Error storing predictions: {e}")
    finally:
        conn.close()
