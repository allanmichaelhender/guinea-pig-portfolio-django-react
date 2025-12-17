import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

const PortfoliosForm = () => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    defaultValues: {
      investment_amount: 0,
      FTSE_weight: 0,
      SNP500_weight: 0,
      NIKKEI225_weight: 0,
    }
  });

  const onSubmit = async (data) => {
    try {
      const response = await api.post('/portfolios/', data);
      alert('Portfolio Created!');
    } catch (error) {
      console.error('Submission failed:', error.response?.data);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="investment-frequency-input-field">
        <label>Investment Frequency:</label>
        <input type="radio" value="monthly" {...register("investment_frequency")} /> Monthly
        <input type="radio" value="yearly" {...register("investment_frequency")} /> Yearly
      </div>

      <input type="date" className="date-input-field" {...register("start_date")} />
      <input type="date" className="date-input-field" {...register("end_date")} />

      <input 
        type="number" 
        step="0.01" 
        className="weight-input" 
        {...register("FTSE_weight")} 
      />

      <button type="submit">Submit Portfolio</button>
    </form>
  );
};

export default PortfoliosForm