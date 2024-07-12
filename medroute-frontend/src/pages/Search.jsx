import React, { useState } from 'react';
import { Box, Heading, Input, Button, VStack, Image } from '@chakra-ui/react';
import logo from '../assets/logo.png'; // Ensure the path is correct

const Search = () => {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = () => {
    // Handle the search logic here
    console.log('Search query:', searchQuery);
  };

  return (
    <Box textAlign="center" py={10} px={6}>
      <Heading as="h1" size="2xl" mb={6}>
        Search
      </Heading>
      <Image
        src={logo}
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
    </Box>
  );
};

export default Search;
