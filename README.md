### Hexlet tests and linter status:
[![Actions Status](https://github.com/ross0maha/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ross0maha/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2e3053157b86113f589e/maintainability)](https://codeclimate.com/github/ross0maha/python-project-49/maintainability)

<div class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="xxBReaj" data-user="Dmitry-Yuroff"  data-prefill='{"title":"Animated text fill with svg text practice","description":"SVG text","tags":["animated-text-fill","svg-text"],"scripts":[],"stylesheets":[]}'>
  <pre data-lang="pug">svg(viewBox="0 0 600 300")
  // Symbol
  symbol#s-text
    text(text-anchor="middle", x="50%", y="50%", dy=".35em")
      | BRAIN GAMES
  // Duplicate symbols
  use.text(xlink:href="#s-text")
  use.text(xlink:href="#s-text")
  use.text(xlink:href="#s-text")
  use.text(xlink:href="#s-text")
  use.text(xlink:href="#s-text")</pre>
  <pre data-lang="scss">$colors: #F2385A, #F5A503, #E9F1DF, #56D9CD, #3AA1BF;
$max: length($colors);
$dash: 70;
$dash-gap: 10;
$dash-space: $dash * ($max - 1) + $dash-gap * $max;
$time: 6s;
$time-step: $time/$max;

/* Main styles */
@import url(https://fonts.googleapis.com/css?family=Open+Sans:800);

.text {
  fill: none;
  stroke-width: 3;
  stroke-linejoin: round;
  stroke-dasharray: $dash $dash-space;
  stroke-dashoffset: 0;
  -webkit-animation: stroke $time infinite linear;
  animation: stroke $time infinite linear;
  
  @for $item from 1 through $max {
    &:nth-child(#{$max}n + #{$item}) {
      $color: nth($colors, $item);
      stroke: $color;
      -webkit-animation-delay: -($time-step * $item);
      animation-delay: -($time-step * $item);
    }
  }
}

@-webkit-keyframes stroke {
  100% {
    stroke-dashoffset: -($dash + $dash-gap) * $max;
  }
}

@keyframes stroke {
  100% {
    stroke-dashoffset: -($dash + $dash-gap) * $max;
  }
}

/* Other styles */
html, body {
  height: 100%;
}

body {
  background: #111;
  background-size: .2em 100%;
  font: 5em/1 Open Sans, Impact;
  text-transform: uppercase;
  margin: 0;
}

svg {
  position: absolute;
  width: 100%;
  height: 100%;
}</pre></div>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

```
              ____            _              ____                           
            | __ ) _ __ __ _(_)_ __        / ___| __ _ _ __ ___   ___  ___ 
            |  _ \| '__/ _` | | '_ \ _____| |  _ / _` | '_ ` _ \ / _ \/ __|
            | |_) | | | (_| | | | | |_____| |_| | (_| | | | | | |  __/\__ \
            |____/|_|  \__,_|_|_| |_|      \____|\__,_|_| |_| |_|\___||___/
```

#### My first project in the He\}\{let school.


### Brain-Even game.

Play demo
![(src/brain-even.gif)|800](src/brain-even.gif)
