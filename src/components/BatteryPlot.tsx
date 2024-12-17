import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import { Battery } from 'lucide-react';

// Simulated data since we can't directly access the Kaggle dataset
const generateSampleData = (cycles: number) => {
  const x = Array.from({ length: cycles }, (_, i) => i + 1);
  const reData = x.map(cycle => 0.015 + 0.001 * Math.log(cycle) + Math.random() * 0.002);
  const rctData = x.map(cycle => 0.025 + 0.003 * Math.log(cycle) + Math.random() * 0.003);
  return { x, reData, rctData };
};

const BatteryPlot: React.FC = () => {
  const [data, setData] = useState<{ x: number[]; reData: number[]; rctData: number[]; }>();

  useEffect(() => {
    const sampleData = generateSampleData(100);
    setData(sampleData);
  }, []);

  if (!data) return <div>Loading...</div>;

  return (
    <div className="w-full max-w-4xl mx-auto p-6">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center gap-2 mb-6">
          <Battery className="w-6 h-6 text-blue-600" />
          <h2 className="text-2xl font-bold text-gray-800">Battery Impedance Analysis</h2>
        </div>
        
        <Plot
          data={[
            {
              x: data.x,
              y: data.reData,
              type: 'scatter',
              mode: 'lines+markers',
              name: 'Electrolyte Resistance (Re)',
              line: { color: '#2563eb' },
            },
            {
              x: data.x,
              y: data.rctData,
              type: 'scatter',
              mode: 'lines+markers',
              name: 'Charge Transfer Resistance (Rct)',
              line: { color: '#dc2626' },
            },
          ]}
          layout={{
            title: 'Battery Impedance Parameters vs. Cycle Number',
            xaxis: {
              title: 'Cycle Number',
              gridcolor: '#f3f4f6',
            },
            yaxis: {
              title: 'Resistance (Ohms)',
              gridcolor: '#f3f4f6',
            },
            plot_bgcolor: 'white',
            paper_bgcolor: 'white',
            hovermode: 'closest',
            showlegend: true,
            legend: {
              x: 0,
              y: 1.2,
              orientation: 'h',
            },
            margin: {
              l: 50,
              r: 50,
              t: 50,
              b: 50,
            },
          }}
          style={{ width: '100%', height: '600px' }}
          config={{ responsive: true }}
        />
        
        <div className="mt-6 text-sm text-gray-600">
          <p>This visualization shows the progression of two key battery impedance parameters over charge/discharge cycles:</p>
          <ul className="list-disc ml-6 mt-2">
            <li><span className="text-blue-600 font-semibold">Electrolyte Resistance (Re)</span>: Represents the ionic conductivity of the electrolyte</li>
            <li><span className="text-red-600 font-semibold">Charge Transfer Resistance (Rct)</span>: Indicates the ease of charge transfer at the electrode-electrolyte interface</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default BatteryPlot;