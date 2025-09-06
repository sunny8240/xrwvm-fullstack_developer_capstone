import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Header from "../Header/Header";

const PostReview = () => {
  const [dealer, setDealer] = useState({});
  const [review, setReview] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [date, setDate] = useState("");
  const [carmodels, setCarmodels] = useState([]);

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0, curr_url.indexOf("postreview"));
  let { id } = useParams();
  let dealer_url = root_url + `djangoapp/dealer/${id}`;
  let review_url = root_url + `djangoapp/add_review`;
  let carmodels_url = root_url + `djangoapp/get_cars`;

  const postreview = async () => {
    let name =
      sessionStorage.getItem("firstname") +
      " " +
      sessionStorage.getItem("lastname");
    if (name.includes("null")) {
      name = sessionStorage.getItem("username");
    }
    if (!model || !review || !date || !year) {
      alert("All fields are required!");
      return;
    }

    let selectedCar = JSON.parse(model);
    let make_chosen = selectedCar.make;
    let model_chosen = selectedCar.model;

    let jsoninput = JSON.stringify({
      name: name,
      dealership: id,
      review: review,
      purchase: true,
      purchase_date: date,
      car_make: make_chosen,
      car_model: model_chosen,
      car_year: year,
    });

    const res = await fetch(review_url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsoninput,
    });

    const json = await res.json();
    if (json.status === 200) {
      window.location.href = window.location.origin + "/dealer/" + id;
    } else {
      alert("Failed to post review. Try again.");
    }
  };

  const get_dealer = async () => {
    const res = await fetch(dealer_url);
    const retobj = await res.json();
    if (retobj.status === 200) {
      let dealerobjs = Array.from(retobj.dealer);
      if (dealerobjs.length > 0) setDealer(dealerobjs[0]);
    }
  };

  const get_cars = async () => {
    const res = await fetch(carmodels_url);
    const retobj = await res.json();
    let carmodelsarr = Array.from(retobj.CarModels);
    setCarmodels(carmodelsarr);
  };

  useEffect(() => {
    get_dealer();
    get_cars();
  }, []);

  const isFormValid = review && model && year && date;

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 text-white font-sans">
      <Header />
      <div className="flex justify-center items-center py-14 px-4">
        <div className="relative bg-gray-800/40 backdrop-blur-xl shadow-2xl rounded-2xl p-10 w-full max-w-3xl border border-cyan-400/30 hover:border-cyan-400/60 transition-all duration-500">
          {/* Glowing top border effect */}
          <div className="absolute -top-1 left-1/2 transform -translate-x-1/2 w-2/3 h-1 bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-600 rounded-full blur-sm animate-pulse"></div>

          <h1 className="text-4xl font-extrabold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 drop-shadow-lg">
            Post a Review for {dealer.full_name}
          </h1>

          {/* Review Textarea */}
          <label className="block mb-2 text-sm font-semibold text-gray-300">
            ✍️ Your Review
          </label>
          <textarea
            className="w-full p-4 rounded-xl bg-black/40 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-cyan-400 focus:outline-none transition-all mb-6 resize-none shadow-inner"
            rows="6"
            placeholder="Share your amazing experience..."
            onChange={(e) => setReview(e.target.value)}
          ></textarea>

          {/* Purchase Date */}
          <label className="block mb-2 text-sm font-semibold text-gray-300">
            📅 Purchase Date
          </label>
          <input
            type="date"
            className="w-full p-3 mb-6 rounded-xl bg-black/40 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-cyan-400 focus:outline-none"
            onChange={(e) => setDate(e.target.value)}
          />

          {/* Car Dropdown */}
          <label className="block mb-2 text-sm font-semibold text-gray-300">
            🚗 Car Make & Model
          </label>
          <select
            className="w-full p-3 mb-6 rounded-xl bg-black/40 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-cyan-400 focus:outline-none"
            value={model}
            onChange={(e) => setModel(e.target.value)}
          >
            <option value="" disabled hidden>
              Choose Car Make and Model
            </option>
            {carmodels.map((carmodel, index) => (
              <option
                key={index}
                value={JSON.stringify({
                  make: carmodel.CarMake,
                  model: carmodel.CarModel,
                })}
              >
                {carmodel.CarMake} {carmodel.CarModel}
              </option>
            ))}
          </select>

          {/* Car Year */}
          <label className="block mb-2 text-sm font-semibold text-gray-300">
            📆 Car Year
          </label>
          <input
            type="number"
            className="w-full p-3 mb-8 rounded-xl bg-black/40 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-cyan-400 focus:outline-none"
            placeholder="e.g. 2023"
            min={2015}
            max={2025}
            onChange={(e) => setYear(e.target.value)}
          />

          {/* Submit Button */}
          <button
            onClick={postreview}
            disabled={!isFormValid}
            className={`w-full py-4 px-6 rounded-xl text-xl font-bold tracking-wide shadow-lg transition-all duration-500 
              ${
                isFormValid
                  ? "bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-600 hover:from-purple-600 hover:to-cyan-400 text-white animate-pulse"
                  : "bg-gray-700 cursor-not-allowed"
              }`}
          >
            🚀 Post Review
          </button>
        </div>
      </div>
    </div>
  );
};

export default PostReview;
