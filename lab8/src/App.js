import React from 'react';
import './App.css';
import axios from 'axios';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            repos: [],
        }
    }

    componentDidMount() {
        axios.get('https://api.github.com/users/Luchik7/repos')
            .then(response => {
                this.setState({repos: response.data});
        })
            .catch(error => {
                console.log(error);
            });
    }

    render() {
    let repos = this.state.repos.map(repo => (
        <li key={repo.id}>{repo.name}</li>
    ));
    return (
        <div>
            <h1>Daria's repositories from registration to now</h1>
            <ul>
                {repos}
            </ul>
        </div>
    );
  }
}

export default App;


