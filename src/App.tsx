import React, { useState } from 'react';
import { 
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  BarChart, Bar, Cell
} from 'recharts';
import { 
  Home, 
  TrendingUp, 
  Settings, 
  BrainCircuit, 
  FileText, 
  PlusCircle,
  Activity,
  ChevronRight,
  Sparkles,
  Zap
} from 'lucide-react';

// Mock data based on housing pipeline features
const marketTrends = [
  { name: 'Jan', price: 450000, prediction: 448000 },
  { name: 'Feb', price: 462000, prediction: 465000 },
  { name: 'Mar', price: 458000, prediction: 460000 },
  { name: 'Apr', price: 475000, prediction: 472000 },
  { name: 'May', price: 489000, prediction: 485000 },
  { name: 'Jun', price: 505000, prediction: 502000 },
  { name: 'Jul', price: 512000, prediction: 515000 },
];

const featureImportance = [
  { name: 'Square Footage', value: 0.45 },
  { name: 'Neighborhood', value: 0.30 },
  { name: 'Age of Property', value: 0.15 },
  { name: 'Market Sentiment', value: 0.10 },
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [prediction, setPrediction] = useState<number | null>(null);
  const [marketingContent, setMarketingContent] = useState<string>('');

  const handlePredict = (e: React.FormEvent) => {
    e.preventDefault();
    // Simulate prediction logic from Python script
    const mockPrice = 450000 + Math.random() * 50000;
    setPrediction(mockPrice);
    setMarketingContent(`This property is predicted to be valued at $${mockPrice.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}.`);
  };

  return (
    <div className="min-h-screen bg-slate-50 flex text-slate-900">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-slate-200 flex flex-col">
        <div className="p-6 flex items-center gap-2 border-b border-slate-100">
          <BrainCircuit className="text-blue-600" size={32} />
          <h1 className="font-bold text-xl tracking-tight">AI Studio X</h1>
        </div>
        
        <nav className="flex-1 p-4 space-y-2">
          <button 
            onClick={() => setActiveTab('dashboard')}
            className={`w-full flex items-center gap-3 px-4 py-2 rounded-lg transition-colors ${activeTab === 'dashboard' ? 'bg-blue-50 text-blue-700 shadow-sm' : 'text-slate-600 hover:bg-slate-50'}`}
          >
            <TrendingUp size={20} />
            <span className="font-medium">Dashboard</span>
          </button>
          <button 
            onClick={() => setActiveTab('pipeline')}
            className={`w-full flex items-center gap-3 px-4 py-2 rounded-lg transition-colors ${activeTab === 'pipeline' ? 'bg-blue-50 text-blue-700 shadow-sm' : 'text-slate-600 hover:bg-slate-50'}`}
          >
            <Activity size={20} />
            <span className="font-medium">Pipeline</span>
          </button>
          <button 
            onClick={() => setActiveTab('marketing')}
            className={`w-full flex items-center gap-3 px-4 py-2 rounded-lg transition-colors ${activeTab === 'marketing' ? 'bg-blue-50 text-blue-700 shadow-sm' : 'text-slate-600 hover:bg-slate-50'}`}
          >
            <FileText size={20} />
            <span className="font-medium">Marketing</span>
          </button>
        </nav>

        <div className="p-4 border-t border-slate-100">
          <div className="bg-slate-900 text-white p-4 rounded-xl space-y-3 relative overflow-hidden">
            <div className="relative z-10">
              <p className="text-xs text-slate-400 font-medium">MODEL STATUS</p>
              <p className="font-bold">Active & Optimized</p>
              <div className="mt-2 flex items-center gap-2 text-xs text-green-400">
                <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span>
                Ready for predictions
              </div>
            </div>
            <Zap className="absolute -right-4 -bottom-4 text-slate-800" size={80} />
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8 overflow-y-auto">
        <header className="flex justify-between items-center mb-8">
          <div>
            <h2 className="text-2xl font-bold">Housing Market Analysis</h2>
            <p className="text-slate-500">Real-time AI-powered property valuation pipeline</p>
          </div>
          <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-blue-700 transition-colors shadow-sm">
            <PlusCircle size={20} />
            New Analysis
          </button>
        </header>

        {activeTab === 'dashboard' && (
          <div className="space-y-6">
            {/* Stats Overview */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div className="flex justify-between items-start mb-4">
                  <div className="p-2 bg-blue-100 rounded-lg text-blue-600">
                    <Home size={24} />
                  </div>
                  <span className="text-green-600 text-sm font-bold flex items-center">
                    +4.2% <ChevronRight size={14} className="-rotate-90" />
                  </span>
                </div>
                <p className="text-slate-500 text-sm font-medium">Avg Market Price</p>
                <h3 className="text-2xl font-bold mt-1">$485,200</h3>
              </div>

              <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div className="flex justify-between items-start mb-4">
                  <div className="p-2 bg-purple-100 rounded-lg text-purple-600">
                    <Activity size={24} />
                  </div>
                  <span className="text-slate-400 text-sm font-medium">MSE: 1542.23</span>
                </div>
                <p className="text-slate-500 text-sm font-medium">Model Confidence</p>
                <h3 className="text-2xl font-bold mt-1">94.8%</h3>
              </div>

              <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div className="flex justify-between items-start mb-4">
                  <div className="p-2 bg-amber-100 rounded-lg text-amber-600">
                    <Settings size={24} />
                  </div>
                  <span className="text-blue-600 text-sm font-medium cursor-pointer hover:underline">Configure</span>
                </div>
                <p className="text-slate-500 text-sm font-medium">Pipeline Runs</p>
                <h3 className="text-2xl font-bold mt-1">1,204</h3>
              </div>
            </div>

            {/* Charts Section */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <h4 className="font-bold mb-6 flex items-center gap-2">
                  <TrendingUp size={18} className="text-blue-600" />
                  Market Price Prediction Accuracy
                </h4>
                <div className="h-[300px] w-full">
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={marketTrends}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                      <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12}} />
                      <YAxis axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12}} tickFormatter={(val) => `$${val/1000}k`} />
                      <Tooltip 
                        contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)'}}
                        formatter={(val: any) => [`$${val.toLocaleString()}`, '']}
                      />
                      <Legend verticalAlign="top" align="right" height={36} iconType="circle" />
                      <Line type="monotone" dataKey="price" name="Actual Price" stroke="#2563eb" strokeWidth={3} dot={{r: 4, fill: '#2563eb'}} activeDot={{r: 6}} />
                      <Line type="monotone" dataKey="prediction" name="AI Prediction" stroke="#94a3b8" strokeWidth={2} strokeDasharray="5 5" dot={false} />
                    </LineChart>
                  </ResponsiveContainer>
                </div>
              </div>

              <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <h4 className="font-bold mb-6 flex items-center gap-2">
                  <BrainCircuit size={18} className="text-purple-600" />
                  AI Feature Importance
                </h4>
                <div className="h-[300px] w-full">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={featureImportance} layout="vertical">
                      <CartesianGrid strokeDasharray="3 3" horizontal={false} stroke="#f1f5f9" />
                      <XAxis type="number" hide />
                      <YAxis dataKey="name" type="category" axisLine={false} tickLine={false} tick={{fill: '#1e293b', fontSize: 12, fontWeight: 500}} width={120} />
                      <Tooltip 
                        cursor={{fill: '#f8fafc'}}
                        contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)'}}
                      />
                      <Bar dataKey="value" radius={[0, 4, 4, 0]} barSize={32}>
                        {featureImportance.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                      </Bar>
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'pipeline' && (
          <div className="bg-white p-8 rounded-xl border border-slate-200 shadow-sm max-w-2xl">
            <h3 className="text-xl font-bold mb-6">Run AI Valuation Analysis</h3>
            <form onSubmit={handlePredict} className="space-y-6">
              <div className="grid grid-cols-2 gap-6">
                <div className="space-y-2">
                  <label htmlFor="sqft" className="text-sm font-medium text-slate-700">Square Footage</label>
                  <input id="sqft" type="number" placeholder="e.g. 2400" className="w-full px-4 py-2 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all" />
                </div>
                <div className="space-y-2">
                  <label htmlFor="neighborhood" className="text-sm font-medium text-slate-700">Neighborhood (Rank 1-10)</label>
                  <input id="neighborhood" type="number" min="1" max="10" placeholder="e.g. 8" className="w-full px-4 py-2 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all" />
                </div>
                <div className="space-y-2">
                  <label htmlFor="age" className="text-sm font-medium text-slate-700">Property Age (Years)</label>
                  <input id="age" type="number" placeholder="e.g. 15" className="w-full px-4 py-2 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all" />
                </div>
                <div className="space-y-2">
                  <label htmlFor="renovation" className="text-sm font-medium text-slate-700">Renovation Grade (1-5)</label>
                  <input id="renovation" type="number" min="1" max="5" placeholder="e.g. 4" className="w-full px-4 py-2 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all" />
                </div>
              </div>
              <button type="submit" className="w-full bg-slate-900 text-white py-3 rounded-lg font-bold flex items-center justify-center gap-2 hover:bg-slate-800 transition-colors shadow-lg">
                <Zap size={20} className="text-amber-400" />
                Calculate AI Valuation
              </button>
            </form>

            {prediction && (
              <div className="mt-8 p-6 bg-blue-50 border border-blue-100 rounded-xl animate-in fade-in slide-in-from-bottom-4 duration-500">
                <p className="text-blue-700 font-medium mb-1">Estimated Market Value</p>
                <h4 className="text-4xl font-black text-blue-900">
                  ${prediction.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                </h4>
                <div className="mt-4 p-4 bg-white rounded-lg border border-blue-100 flex items-start gap-3">
                  <Sparkles className="text-blue-500 mt-1 shrink-0" size={20} />
                  <p className="text-sm text-slate-600 leading-relaxed italic">
                    "{marketingContent}"
                  </p>
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === 'marketing' && (
          <div className="space-y-6">
            <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
              <h3 className="text-xl font-bold mb-4">Marketing Content Hub</h3>
              <p className="text-slate-500 mb-6">AI-generated descriptions and selling points based on market analysis.</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {[1, 2, 3, 4].map((i) => (
                  <div key={i} className="group border border-slate-100 p-6 rounded-xl hover:border-blue-200 hover:bg-blue-50 transition-all cursor-pointer">
                    <div className="flex justify-between items-start mb-4">
                      <div className="text-xs font-bold uppercase tracking-wider text-slate-400 group-hover:text-blue-500">Property Listing #{1000 + i}</div>
                      <button className="text-slate-300 group-hover:text-blue-400"><PlusCircle size={18} /></button>
                    </div>
                    <p className="text-slate-700 font-medium line-clamp-2 mb-4 italic">
                      "This stunning property features modern AI-optimized layouts and is predicted to be valued at $492,400.00..."
                    </p>
                    <div className="flex gap-2">
                      <span className="px-2 py-1 bg-slate-100 text-slate-500 rounded text-[10px] font-bold uppercase">Modern</span>
                      <span className="px-2 py-1 bg-slate-100 text-slate-500 rounded text-[10px] font-bold uppercase">Prime Location</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
