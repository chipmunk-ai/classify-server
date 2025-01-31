# Chipmunk Classify Server

This server is used to analyze data with specific features to predict "homerun" and "strike" outcomes. It processes incoming requests and returns predictions in JSON format.

## Endpoints

### [POST] /predict

This endpoint is used to send data to the server and receive predictions for "homerun" or "strike." When making a request, you need to send the data in JSON format.

#### 1. Homerun Prediction Request

**Request:**

```json
{
  "request_homerun": [
    100.1, 382, 32
  ]
}
```

- **request_homerun**: This field contains the data used to make a "homerun" prediction. The data represents the following features in order:
  - `100.1`: exit_velocity
  - `382`: hit_distance
  - `32`: launch_angle

**Response:**

```json
{
  "homerun_predictions": [
    0
  ]
}
```

- **homerun_predictions**: This field contains the "homerun" prediction result. It returns a value such as `0` or `1`. Typically, `0` indicates "no homerun," while `1` indicates "homerun."

#### 2. Strike Prediction Request

**Request:**

```json
{
  "request_strike": [
    96.6, 2442, -0.35, 1.45, 0.87, 1.76, 14
  ]
}
```

- **request_strike**: This field contains the data used to make a "strike" prediction. The data represents the following features in order:
  - `96.6`: release_speed
  - `2442`: release_spin_rate
  - `-0.35`: pfx_x
  - `1.45`: pfx_z
  - `0.87`: plate_x
  - `1.76`: plate_z
  - `14`: zone

**Response:**

```json
{
  "strike_predictions": [
    0
  ]
}
```

- **strike_predictions**: This field contains the "strike" prediction result. It returns a value such as `0` or `1`. Typically, `0` indicates "no strike," while `1` indicates "strike."

## Example Usage

### Example Request Using cURL

**Homerun Prediction Request:**

```bash
curl -X POST http://localhost:1881/predict \
-H "Content-Type: application/json" \
-d '{
  "request_homerun": [
    100.1, 382, 32
  ]
}'
```

**Strike Prediction Request:**

```bash
curl -X POST http://localhost:1881/predict \
-H "Content-Type: application/json" \
-d '{
  "request_strike": [
    96.6, 2442, -0.35, 1.45, 0.87, 1.76, 14
  ]
}'
```

## Error Responses

- **400 Bad Request**: This error is returned when the request contains missing or invalid data.
- **500 Internal Server Error**: This error is returned when an issue occurs on the server side.

## License
Unlicensed.