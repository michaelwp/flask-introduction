import React, {useState, useEffect} from 'react';
import axios from 'axios';

export default function Email() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    getEmailList()
  }, []);

  const getEmailList = () => {
    axios.get('http://127.0.0.1:5000/emails')
      .then(res => {
        setEmails(res.data.data);
      })
  }

  return (
    <>
      <h2>Email List</h2>
      <ul>
        {emails.map((email, id) => (
          <li key={id}>{email}</li>
        ))}
      </ul>
    </>
  );
}
