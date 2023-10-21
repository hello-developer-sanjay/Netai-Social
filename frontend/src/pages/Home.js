import React from 'react';
import MessageForm from '../components/MessageForm';
import MessageList from '../components/MessageList';

const Home = () => {
    return (
        <div>
            <MessageForm />
            <MessageList />
        </div>
    );
};

export default Home;
