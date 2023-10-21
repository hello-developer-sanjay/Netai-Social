import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Chart from 'chart.js/auto';
import './MessageList.css'; // Import the CSS file

const MessageList = () => {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const fetchMessages = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/messages');
                setMessages(response.data);
                updateChart(response.data);
            } catch (error) {
                console.error('Error fetching messages:', error);
            }
        };
        fetchMessages();
    }, []);

    const updateChart = (data) => {
        const ctx = document.getElementById('sentimentChart').getContext('2d');
        const sentiments = data.map(message => message.sentiment);

        const sentimentCounts = {
            'POSITIVE': 0,
            'NEGATIVE': 0,
            'NEUTRAL': 0,
        };

        sentiments.forEach(sentiment => {
            sentimentCounts[sentiment]++;
        });

        const chartData = {
            labels: Object.keys(sentimentCounts),
            datasets: [
                {
                    data: Object.values(sentimentCounts),
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(255, 206, 86, 1)',
                    ],
                    borderWidth: 1,
                },
            ],
        };

        new Chart(ctx, {
            type: 'bar',
            data: chartData,
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: Math.max(...Object.values(sentimentCounts)) + 1,
                    },
                },
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: 'Sentiment Analysis',
                    },
                },
            },
        });
    };

    return (
        <div className="chart-container"> {/* Apply CSS class to the chart container */}
            <h2>Messages</h2>
            <ul>
                {messages.map((message, index) => (
                    <li key={index}>
                        <strong>Sentiment:</strong> {message.sentiment} <br />
                        <strong>Message:</strong> {message.text}
                    </li>
                ))}
            </ul>
            <canvas id="sentimentChart" width="400" height="200"></canvas>
        </div>
    );
};

export default MessageList;
