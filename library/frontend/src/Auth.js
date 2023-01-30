import React from 'react'

class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {login: '', password: ''}
    }

    handleChange(event) {
        this.setState(
                  }
                [event.target.name]: event.target.value
            }
       )
    }

    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
        <form onSubmit={(event:FormEvent<HTMLFormElement> ) => this.handleSubmit(event)}>
            <input type="text" name="login" placeholder="login" value={this.state.login}
                   onChange={(event:ChangeEvent<...> )=> this.handleChange(event)}/>
            <input type="password" name="password" placeholder="password" value={this.state.password}
                   onChange={(event:ChangeEvent<HTMLInputElement>
                   )=> this.handleChange(event)}/>
            <input type="submit" value="Login"/>
        </form>
        )
    }
}

export default LoginForm