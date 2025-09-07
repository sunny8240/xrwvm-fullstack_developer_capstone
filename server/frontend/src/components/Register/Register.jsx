import React, { useState } from "react";
import "./Register.css";
import user_icon from "../assets/person.png";
import email_icon from "../assets/email.png";
import password_icon from "../assets/password.png";
import close_icon from "../assets/close.png";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [loading, setLoading] = useState(false);

  const goHome = () => window.location.href = "/";

  const register = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(window.location.origin + "/djangoapp/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userName, password, firstName, lastName, email }),
      });
      const json = await res.json();
      setLoading(false);
      if (json.status) {
        sessionStorage.setItem("username", json.userName);
        window.location.href = "/";
      } else {
        alert(json.error || "Registration failed!");
      }
    } catch {
      setLoading(false);
      alert("Something went wrong!");
    }
  };

  return (
    <div className="register_container">
      <div className="register_card">
        <div className="header">
          <h2>Sign Up</h2>
          <img src={close_icon} alt="close" className="close_icon" onClick={goHome} />
        </div>
        <form className="register_form" onSubmit={register}>
          <div className="input_group"><img src={user_icon} alt="User"/><input type="text" placeholder="Username" value={userName} onChange={e => setUserName(e.target.value)} required/></div>
          <div className="input_group"><img src={user_icon} alt="First Name"/><input type="text" placeholder="First Name" value={firstName} onChange={e => setFirstName(e.target.value)} required/></div>
          <div className="input_group"><img src={user_icon} alt="Last Name"/><input type="text" placeholder="Last Name" value={lastName} onChange={e => setLastName(e.target.value)} required/></div>
          <div className="input_group"><img src={email_icon} alt="Email"/><input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required/></div>
          <div className="input_group"><img src={password_icon} alt="Password"/><input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required/></div>
          <button className="register_btn" type="submit" disabled={loading}>{loading ? "Signing Up..." : "Register"}</button>
        </form>
      </div>
      <div className="animated_bg">
        <div className="circle c1"></div>
        <div className="circle c2"></div>
        <div className="circle c3"></div>
        <div className="circle c4"></div>
      </div>
    </div>
  );
};

export default Register;
