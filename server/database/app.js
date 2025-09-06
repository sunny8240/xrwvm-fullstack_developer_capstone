// app.js
const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 3030;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Load JSON data
let reviews_data = [];
let dealerships_data = [];

try {
  reviews_data = JSON.parse(fs.readFileSync("reviews.json", 'utf8'))['reviews'];
  dealerships_data = JSON.parse(fs.readFileSync("dealerships.json", 'utf8'))['dealerships'];
} catch (err) {
  console.error("Error reading JSON files:", err);
}

// MongoDB connection
mongoose.connect("mongodb://mongo_db:27017/", { dbName: 'dealershipsDB' })
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.error("MongoDB connection error:", err));

// Import Mongoose models
const Reviews = require('./review');       // Make sure review.js defines the Reviews schema
const Dealerships = require('./dealership'); // Make sure dealership.js defines the Dealerships schema

// Load initial data
(async () => {
  try {
    if (reviews_data.length > 0) {
      await Reviews.deleteMany({});
      await Reviews.insertMany(reviews_data);
    }

    if (dealerships_data.length > 0) {
      await Dealerships.deleteMany({});
      await Dealerships.insertMany(dealerships_data);
    }

    console.log("Initial data loaded successfully");
  } catch (error) {
    console.error("Error inserting initial data:", error);
  }
})();

// Routes

// Home
app.get('/', (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// Fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error fetching reviews' });
  }
});

// Fetch reviews by dealer ID
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const dealerId = parseInt(req.params.id);
    const documents = await Reviews.find({ dealership: dealerId });
    res.json(documents);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error fetching dealer reviews' });
  }
});

// Fetch all dealers
app.get('/fetchDealers', async (req, res) => {
  try {
    const dealers = await Dealerships.find();
    res.json(dealers);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error fetching dealers' });
  }
});

// Fetch dealers by state (case-insensitive)
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const state = req.params.state;
    const dealers = await Dealerships.find({ state: { $regex: new RegExp(`^${state}$`, 'i') } });
    res.json(dealers);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error fetching dealers by state' });
  }
});

// Fetch dealer by ID
app.get('/fetchDealer/:id', async (req, res) => {
    try {
      const param = req.params.id;
      let dealer;
  
      // Try numeric match first
      if (!isNaN(param)) {
        dealer = await Dealerships.findOne({ id: parseInt(param) });
      }
  
      // Fallback to string match
      if (!dealer) {
        dealer = await Dealerships.findOne({ id: param });
      }
  
      if (!dealer) return res.status(404).json({ message: 'Dealer not found' });
      res.json(dealer);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Error fetching dealer by ID' });
    }
  });
  
  
  

// Insert a new review
app.post('/insert_review', async (req, res) => {
  try {
    const data = req.body;

    // Generate new ID
    const lastDoc = await Reviews.findOne().sort({ id: -1 });
    const new_id = lastDoc ? lastDoc.id + 1 : 1;

    const review = new Reviews({
      id: new_id,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
