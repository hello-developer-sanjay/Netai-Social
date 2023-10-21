import React, { useState } from 'react';
import axios from 'axios';
import './MessageForm.css';

const MessageForm = () => {
    const [text, setText] = useState('');
    const [aspects, setAspects] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:5000/api/messages', { text, aspects });
            setText('');
            setAspects([]);  // Reset aspects after submission
        } catch (error) {
            console.error('Error submitting message:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Enter your message"
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <input
                type="text"
                placeholder="Enter aspects (comma separated)"
                value={aspects.join(',')}
                onChange={(e) => setAspects(e.target.value.split(','))}
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default MessageForm;
