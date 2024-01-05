import React, {useState, useEffect} from 'react';
import axios from 'axios';

export default function Email() {
  const [emails, setEmails] = useState([]);
  const [email, setEmail] = useState("");

  useEffect(() => {
    getEmailList()
  }, [emails]);

  const getEmailList = () => {
    axios.get('http://127.0.0.1:5000/emails')
      .then(res => {
        setEmails(res.data.data);
      })
  }

  const addEmail = (email) => {
    axios.post('http://127.0.0.1:5000/emails', {
        email: email,
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  return (
    <>
      <h2>Email List</h2>
      <ul>
        {emails.map((email, id) => (
          <li key={id}>{email}</li>
        ))}
      </ul>
      <p>
        <h2>New Email</h2>
        <input value={email} onChange={e => setEmail(e.target.value)}/>
        <button onClick={() => addEmail(email)}>Add</button>
      </p>
    </>
  );
}
