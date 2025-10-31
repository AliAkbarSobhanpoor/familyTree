import React from "react";
import * as d3 from "d3"; // npm install d3
import * as f3 from "family-chart"; // npm install family-chart@0.9.0
import "family-chart/styles/family-chart.css";

export default class FamilyTree extends React.Component {
  cont = React.createRef();

  componentDidMount() {
    if (!this.cont.current) return;

    // Fetch data from your Django API
    fetch("http://127.0.0.1:8000/api/v1/persons/")
      .then((res) => res.json())
      .then((data) => createChart(data))
      .catch((err) => console.error("Error fetching data:", err));

    function createChart(data) {
      // Create the main chart
      const f3Chart = f3
        .createChart("#FamilyChart", data)
        .setTransitionTime(1000)
        .setCardXSpacing(250)
        .setCardYSpacing(150)
        .setSingleParentEmptyCard(false, { label: "ADD" })
        .setShowSiblingsOfMain(false)
        .setOrientationVertical();

      // Configure card appearance
      const f3Card = f3Chart
        .setCardHtml()
        .setCardDisplay([
          ["fn", "ln"],
          ["birthday"],
        ])
        .setCardDim(null)
        .setMiniTree(true)
        .setStyle("imageRect");

      // Configure editable tree features
      const f3EditTree = f3Chart.editTree()
        .fixed(true)
        .setFields(["fn", "ln", "desc"])
        .setEditFirst(false)
        .setCardClickOpen(f3Card);

      f3EditTree.setNoEdit();

      // Render tree
      f3Chart.updateTree({ initial: true });
      f3Chart.updateTree({ initial: true });
    }
  }

  render() {
    return (
      <div
        className="f3"
        id="FamilyChart"
        ref={this.cont}
        style={{
          width: "100%",
          height: "80vh",
          margin: "auto",
          backgroundColor: "rgb(33,33,33)",
          color: "#fff",
        }}
      ></div>
    );
  }
}
