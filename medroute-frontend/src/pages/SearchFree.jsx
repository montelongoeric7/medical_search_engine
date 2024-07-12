import React, { useState } from 'react';
import { Box, Heading, Input, Button, VStack, Image, Text } from '@chakra-ui/react';
import logo2 from '../assets/logo2.png';

const SearchFree = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResponse, setSearchResponse] = useState('');

  const handleSearch = async () => {
    try {
      const response = await fetch('http://localhost:8000/search_router/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: searchQuery }), // Ensure the payload matches the expected format
      });

      if (!response.ok) {
        throw new Error('Failed to fetch search results');
      }

      const data = await response.json();
      setSearchResponse(data.query);
    } catch (error) {
      console.error('Error during search:', error);
      setSearchResponse('Error fetching search results');
    }
  };

  return (
    <Box textAlign="center" py={10} px={6}>
      <Heading as="h1" size="2xl" mb={6}>
        Search
      </Heading>
      <Image
        src={logo2}
        alt="Logo"
        mx="auto"
        mb={6}
        mt={6}
        boxSize="150px"
      />
      <VStack spacing={4} align="center">
        <Input
          variant="outline"
          placeholder="Type your search query..."
          size="lg"
          width="100%"
          maxWidth="600px"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <Button
          colorScheme="teal"
          size="lg"
          onClick={handleSearch}
        >
          Search
        </Button>
      </VStack>
      {searchResponse && (
        <Box mt={6} textAlign="left" maxWidth="600px" mx="auto">
          <Text fontSize="lg">{searchResponse}</Text>
        </Box>
      )}
    </Box>
  );
};

export default SearchFree;
