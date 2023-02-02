'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return (
      <button onClick={() => {
        this.setState({ liked: true });
        this.props.setText("You hit the like button");
      }}>
        Like
      </button>);
  }
}


function LikeText(props) {
    return <p>{props.text}</p>
}


class LikeForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { text: "This is some default text" };
  }
  render() {

    return <div>
      <LikeButton setText={(text) => this.setState({ text: text })} />
      <LikeText text={this.state.text} />
    </div>;
  }
}


const domContainer = document.querySelector('#like_button_container');
const root = ReactDOM.createRoot(domContainer);
root.render(<LikeForm />);

// const container = document.querySelector("#like_button_adjacent");
// const root2 = ReactDOM.createRoot(container);
// root2.render(<Form text="HELLO"/>);